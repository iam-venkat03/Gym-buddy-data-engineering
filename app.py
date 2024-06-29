from flask import Flask, render_template, request, redirect, url_for, session, flash
import sqlite3
import numpy as np
import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.preprocessing import OneHotEncoder, StandardScaler
from sklearn.preprocessing import MinMaxScaler

app = Flask(__name__)
app.secret_key = 'your_secret_key'

# Mock database
users = {
    'user1': '123',
    'user2': '123'
}

# Database setup
def init_db():
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()
    
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS profiles (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT,
            mail_id TEXT,
            name TEXT,
            age INTEGER,
            gender TEXT,
            height INTEGER,
            weight INTEGER,
            preferred_time1 TEXT,
            preferred_time2 TEXT,
            goals TEXT,
            experience_in_gym TEXT,
            workout_duration TEXT,
            pref_gym_location TEXT,
            travel_freq TEXT,
            pref_buddy_age INTEGER,
            pref_buddy_gender TEXT
        )
    ''')
    conn.commit()
    conn.close()

init_db()

@app.route('/')
def index():
    return render_template('login.html')

@app.route('/login', methods=['POST'])
def login():
    username = request.form['username']
    password = request.form['password']

    # Simple authentication
    if username in users and users[username] == password:
        session['username'] = username
        return redirect(url_for('profile'))
    else:
        flash('Invalid credentials', 'error')
        return redirect(url_for('index'))

@app.route('/profile')
def profile():
    if 'username' in session:
        return render_template('profile.html')
    else:
        return redirect(url_for('index'))

@app.route('/review', methods=['POST'])
def review():
    if 'username' in session:
        profile_data = {
            'username': session.get('username'),
            'mail_id': request.form['mail_id'],
            'name': request.form['name'],
            'age': request.form['age'],
            'gender': request.form['gender'],
            'height': request.form['height'],
            'weight': request.form['weight'],
            'preferred_time1': request.form['preferred-time1'],
            'preferred_time2': request.form['preferred-time2'],
            'goals': request.form['goals'],
            'experience_in_gym': request.form['experience-in-gym'],
            'workout_duration': request.form['workout-duration'],
            'pref_gym_location': request.form['pref-gym-location'],
            'travel_freq': request.form['travel-freq'],
            'pref_buddy_age': request.form['pref-buddy-age'],
            'pref_buddy_gender': request.form['pref-buddy-gender']
        }
        return render_template('review.html', profile_data=profile_data)
    else:
        return redirect(url_for('index'))

@app.route('/submit-profile', methods=['POST'])
def submit_profile():
    if 'username' in session:
        profile_data = {
            'username': session.get('username'),
            'mail_id_full': request.form['mail_id'],  # Store the full mail ID
            'mail_id_masked': '*' * (len(request.form['mail_id']) - 3) + request.form['mail_id'][-3:],  # Store the masked mail ID
            'name': request.form['name'],
            'age': request.form['age'],
            'gender': request.form['gender'],
            'height': request.form['height'],
            'weight': request.form['weight'],
            'preferred_time1': request.form['preferred-time1'],
            'preferred_time2': request.form['preferred-time2'],
            'goals': request.form['goals'],
            'experience_in_gym': request.form['experience-in-gym'],
            'workout_duration': request.form['workout-duration'],
            'pref_gym_location': request.form['pref-gym-location'],
            'travel_freq': request.form['travel-freq'],
            'pref_buddy_age': request.form['pref-buddy-age'],
            'pref_buddy_gender': request.form['pref-buddy-gender']
        }
        
        conn = sqlite3.connect('database.db')
        cursor = conn.cursor()
        cursor.execute('''INSERT INTO profiles (username, mail_id, name, age, gender, height, weight, preferred_time1, preferred_time2, goals, experience_in_gym, workout_duration, pref_gym_location, travel_freq, pref_buddy_age, pref_buddy_gender) 
                          VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)''', 
                       (profile_data['username'], profile_data['mail_id_full'], profile_data['name'], profile_data['age'], profile_data['gender'], profile_data['height'], profile_data['weight'], profile_data['preferred_time1'], profile_data['preferred_time2'], profile_data['goals'], profile_data['experience_in_gym'], profile_data['workout_duration'], profile_data['pref_gym_location'], profile_data['travel_freq'], profile_data['pref_buddy_age'], profile_data['pref_buddy_gender']))
        conn.commit()
        conn.close()

        return redirect(url_for('view_profiles'))
    else:
        return redirect(url_for('index'))

@app.route('/view-profiles')
def view_profiles():
    if 'username' in session:
        conn = sqlite3.connect('database.db')
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM profiles")
        profiles = cursor.fetchall()
        conn.close()
        return render_template('view_profiles.html', profiles=profiles)
    else:
        return redirect(url_for('index'))


@app.route('/recommend-buddy-for-user', methods=['POST'])
def recommend_buddy_for_user():
    if 'username' in session:
        profile_id = request.form['profile_id']
        
        conn = sqlite3.connect('database.db')
        cursor = conn.cursor()
        
        # Fetch the selected user profile
        cursor.execute("SELECT * FROM profiles WHERE id = ?", (profile_id,))
        selected_user = cursor.fetchone()
        
        if selected_user is None:
            flash('Selected profile not found.', 'error')
            return redirect(url_for('view_profiles'))

        # Fetch all profiles except the selected user
        cursor.execute("SELECT * FROM profiles WHERE id != ?", (profile_id,))
        other_users = cursor.fetchall()
        conn.close()
        
        if not other_users:
            flash('No other users found.', 'error')
            return redirect(url_for('view_profiles'))

        # Convert profiles to pandas DataFrame for easier manipulation
        columns = ['id', 'username', 'mail_id', 'name', 'age', 'gender', 'height', 'weight', 'preferred_time1', 'preferred_time2', 'goals', 'experience_in_gym', 'workout_duration', 'pref_gym_location', 'travel_freq', 'pref_buddy_age', 'pref_buddy_gender']
        all_users_df = pd.DataFrame([selected_user] + list(other_users), columns=columns)

        # Separate numerical and categorical columns
        numerical_columns = ['age', 'height', 'weight', 'pref_buddy_age']
        categorical_columns = ['gender', 'preferred_time1', 'preferred_time2', 'goals', 'experience_in_gym', 'workout_duration', 'pref_gym_location', 'travel_freq', 'pref_buddy_gender']

        # Handle numerical data
        numerical_data = all_users_df[numerical_columns].astype(float)
        scaler = StandardScaler()
        scaled_numerical_data = scaler.fit_transform(numerical_data)

        # Handle categorical data with one-hot encoding
        categorical_data = all_users_df[categorical_columns]
        encoder = OneHotEncoder(sparse_output=False)
        encoded_categorical_data = encoder.fit_transform(categorical_data)

        # Assign weights to different features (weights can be adjusted based on feature importance)
        numerical_weights = np.array([1.0, 1.0, 1.0, 1.0])  # Adjust weights for numerical columns
        categorical_weights = np.ones(encoded_categorical_data.shape[1])  # Adjust weights for categorical columns
        combined_weights = np.concatenate((numerical_weights, categorical_weights))

        # Combine numerical and encoded categorical data
        combined_data = np.hstack((scaled_numerical_data, encoded_categorical_data)) * combined_weights

        # Calculate cosine similarity
        selected_user_data = combined_data[0].reshape(1, -1)
        other_users_data = combined_data[1:]
        similarity_scores = cosine_similarity(selected_user_data, other_users_data)[0]

        # Combine the other users with their similarity scores
        buddies_with_scores = [(other_users[i], similarity_scores[i]) for i in range(len(other_users))]

        # Sort the buddies by similarity score in descending order
        buddies_with_scores = sorted(buddies_with_scores, key=lambda x: x[1], reverse=True)

        return render_template('recommend_buddy.html', current_user=selected_user, buddies_with_scores=buddies_with_scores)
    else:
        return redirect(url_for('index'))
    
if __name__ == '__main__':
    app.run(debug=True)
