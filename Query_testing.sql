-- 1 - BMI Calculation for Users
SELECT
  ROUND(((weight/(height*height)) * 10000), 4) AS BMI,
  a.ID,
  b.user_ID
FROM
  gentle-ally-426115-i2.final_gymbuddy_dataset.fact_table a,
  gentle-ally-426115-i2.final_gymbuddy_dataset.userprofile_dim b
WHERE
  a.user_ID = b.user_id
ORDER BY
  ID ASC;

-- 2 - Total Gym Members by Fitness Goals
SELECT
  COUNT(*) AS Total_count,
  Goals
FROM
  gentle-ally-426115-i2.final_gymbuddy_dataset.Gym_dim
GROUP BY
  Goals;

-- 3 - Average Age of Gym Members
SELECT
  AVG(Age)
FROM
  gentle-ally-426115-i2.final_gymbuddy_dataset.userprofile_dim;

-- 4 - Calculate average age of users based on the goals
SELECT
  gym.goals AS Goals,
  ROUND(AVG(temp_table.age), 2) AS Avg_Age
FROM (
  SELECT
    fact.gym_id,
    user.age
  FROM
    gentle-ally-426115-i2.final_gymbuddy_dataset.fact_table AS fact
  INNER JOIN
    gentle-ally-426115-i2.final_gymbuddy_dataset.userprofile_dim AS user
  USING
    (user_id)) AS temp_table
JOIN
  gentle-ally-426115-i2.final_gymbuddy_dataset.Gym_dim AS gym
USING
  (gym_id)
GROUP BY
  Goals
ORDER BY
  Avg_Age;

-- 5 - Find total number of users based on the Preferred location
SELECT
  Preferred_Gym_Location,
  COUNT(*) AS Total_count
FROM
  gentle-ally-426115-i2.final_gymbuddy_dataset.Preference_dim
GROUP BY
  Preferred_Gym_Location
ORDER BY
  Total_count DESC;

-- 6 - Group the users based on the Preferrence_Time 1
SELECT
  Preferred_Time_1,
  COUNT(*) AS Total_count
FROM
  gentle-ally-426115-i2.final_gymbuddy_dataset.time_dim
GROUP BY
  Preferred_Time_1
ORDER BY
  Total_count DESC;

-- 7 - Group the users based on the Preferrence_Time 2
SELECT
  Preferred_Time_2,
  COUNT(*) AS Total_count
FROM
  gentle-ally-426115-i2.final_gymbuddy_dataset.time_dim
GROUP BY
  Preferred_Time_2
ORDER BY
  Total_count DESC;

-- 8 - Finding the total number of users and their preferred time
  --method 1
WITH
  Combined_Times AS (
  SELECT
    Preferred_Time_1 AS Preferred_Time,
    COUNT(*) AS Total_count
  FROM
    gentle-ally-426115-i2.final_gymbuddy_dataset.time_dim
  GROUP BY
    Preferred_Time_1
  UNION ALL
  SELECT
    Preferred_Time_2 AS Preferred_Time,
    COUNT(*) AS Total_count
  FROM
    gentle-ally-426115-i2.final_gymbuddy_dataset.time_dim
  GROUP BY
    Preferred_Time_2 )
SELECT
  Preferred_Time,
  SUM(Total_count) AS Total_count
FROM
  combined_times
GROUP BY
  Preferred_Time
ORDER BY
  Total_count DESC;

  -- method 2
SELECT
  Preferred_Time,
  SUM(Total_count) AS Total_count
FROM (
  SELECT
    Preferred_Time_1 AS Preferred_Time,
    COUNT(*) AS Total_count
  FROM
    gentle-ally-426115-i2.final_gymbuddy_dataset.time_dim
  GROUP BY
    Preferred_Time_1
  UNION ALL
  SELECT
    Preferred_Time_2 AS Preferred_Time,
    COUNT(*) AS Total_count
  FROM
    gentle-ally-426115-i2.final_gymbuddy_dataset.time_dim
  GROUP BY
    Preferred_Time_2 )
GROUP BY
  Preferred_Time
ORDER BY
  Total_count DESC;