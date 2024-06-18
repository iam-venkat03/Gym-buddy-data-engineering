import pandas as pd
if 'transformer' not in globals():
    from mage_ai.data_preparation.decorators import transformer
if 'test' not in globals():
    from mage_ai.data_preparation.decorators import test


@transformer
def transform(df, *args, **kwargs):
    """
    Template code for a transformer block.

    Add more parameters to this function if this block has multiple parent blocks.
    There should be one parameter for each output variable from each parent block.

    Args:
        data: The output from the upstream parent block
        args: The output from any additional upstream blocks (if applicable)

    Returns:
        Anything (e.g. data frame, dictionary, array, int, str, etc.)
    """
    # Specify your transformation logic here

    df.rename(columns={'ï»¿ID' :'ID'},inplace=True)
    df.rename(columns={'Height (cm)' :'Height'},inplace=True)
    df.rename(columns={'Weight (kg)' :'Weight'},inplace=True)

    userprofile_dim = df[['Mail ID', 'Name', 'Age', 'Gender', 'Travel Frequency']].reset_index(drop=True)
    userprofile_dim['user_id'] = userprofile_dim.index

    time_dim = df[['Preferred Time 1', 'Preferred Time 2']].reset_index(drop=True)
    time_dim['Time_ID'] = time_dim.index

    Preference_dim = df[['Preferred Gym Location', 'Preferred Buddy Age', 'Preferred Buddy Gender']].reset_index(drop=True)    
    Preference_dim['Preference_ID'] = Preference_dim.index

    Gym_dim = df[['Goals', 'Workout Duration', 'Experience in Gym']].reset_index(drop=True)
    Gym_dim['Gym_ID'] = Gym_dim.index

    df = df.drop_duplicates(subset=['Mail ID', 'Name', 'Age', 'Gender', 'Travel Frequency'])
    userprofile_dim = userprofile_dim.drop_duplicates(subset=['Mail ID', 'Name', 'Age', 'Gender', 'Travel Frequency'])
    time_dim = time_dim.drop_duplicates(subset=['Preferred Time 1', 'Preferred Time 2'])
    Preference_dim = Preference_dim.drop_duplicates(subset=['Preferred Gym Location', 'Preferred Buddy Age', 'Preferred Buddy Gender'])
    Gym_dim = Gym_dim.drop_duplicates(subset=['Goals', 'Workout Duration', 'Experience in Gym'])


    fact_table = df.merge(userprofile_dim, on=['Mail ID', 'Name', 'Age', 'Gender', 'Travel Frequency']) \
            .merge(time_dim, on=['Preferred Time 1', 'Preferred Time 2']) \
            .merge(Preference_dim, on=['Preferred Gym Location', 'Preferred Buddy Age', 'Preferred Buddy Gender']) \
            .merge(Gym_dim, on=['Goals', 'Workout Duration', 'Experience in Gym']) \
            [['ID', 'user_id', 'Time_ID', 'Preference_ID', 'Gym_ID', 'Height', 'Weight']]

    print(fact_table)

    temp_variable = {"userprofile_dim":userprofile_dim.to_dict(orient="dict"),
    "time_dim":time_dim.to_dict(orient="dict"),
    "Preference_dim":Preference_dim.to_dict(orient="dict"),
    "Gym_dim":Gym_dim.to_dict(orient="dict"),
    "fact_table":fact_table.to_dict("dict")}

    print(len(temp_variable))
    length_dict = {key: len(value) for key, value in temp_variable.items()}
    print(length_dict)

    print(temp_variable)
    
    return temp_variable


    

@test
def test_output(output, *args) -> None:
    """
    Template code for testing the output of the block.
    """
    assert output is not None, 'The output is undefined'
