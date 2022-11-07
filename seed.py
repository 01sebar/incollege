import sqlite3
con = sqlite3.connect("incollege.db")
cur = con.cursor()
# Create `users` table
cur.execute("""
DROP TABLE IF EXISTS `users`;
""")
cur.execute("""
CREATE TABLE `users` (
  `user_id` INTEGER PRIMARY KEY NOT NULL,
  `user_username` varchar(32) NOT NULL,
  `user_password` varchar(12) NOT NULL,
  `user_firstname` varchar(32) NOT NULL,
  `user_lastname` varchar(32) NOT NULL,
  `user_university` varchar(64) NOT NULL,
  `user_major` varchar(64) NOT NULL,
  `user_Type` INTEGER NOT NULL
)
""")
# Create `jobs` table
cur.execute("""
DROP TABLE IF EXISTS `jobs`;
""")
cur.execute("""
CREATE TABLE `jobs` (
  `job_id` INTEGER PRIMARY KEY NOT NULL,
  `job_title` varchar(32) NOT NULL,
  `job_description` varchar(256) NOT NULL,
  `job_employer` varchar(32) NOT NULL,
  `job_location` varchar(64) NOT NULL,
  `job_salary` varchar(64) NOT NULL,
  `job_user_id` INTEGER NOT NULL,
  FOREIGN KEY(job_user_id) REFERENCES users(user_id)
)
""")
# Create `settings` table
cur.execute("""
DROP TABLE IF EXISTS `settings`;
""")
cur.execute("""
CREATE TABLE `settings` (
  `setting_id` INTEGER PRIMARY KEY NOT NULL,
  `setting_key` varchar(32) NOT NULL,
  `setting_value` varchar(32) NOT NULL,
  `setting_user_id` INTEGER NOT NULL,
  FOREIGN KEY(setting_user_id) REFERENCES users(user_id)
)
""")

#create jobsApplied table
cur.execute("""
DROP TABLE IF EXISTS `jobsApplied`;
""")
cur.execute("""
CREATE TABLE `jobsApplied` (
  `job_applied_key` INTEGER PRIMARY KEY NOT NULL,
  `user_id` INTEGER NOT NULL,
  `job_id` INTEGER NOT NULL,
  `graduation_date` varchar(32) NOT NULL,
  `starting_date` varchar(32) NOT NULL,
  `about_paragraph` varchar(256) NOT NULL,
  'status' BOOLEAN,
  FOREIGN KEY(user_id) REFERENCES users(user_id)
)
""")
#create jobsInterested table
cur.execute("""
DROP TABLE IF EXISTS `jobsInterested`;
""")
cur.execute("""
CREATE TABLE `jobsInterested` (
  `job_interested_key` INTEGER PRIMARY KEY NOT NULL,
  `user_id` INTEGER NOT NULL,
  `job_id` INTEGER NOT NULL,
  FOREIGN KEY(user_id) REFERENCES users(user_id)
  FOREIGN KEY(job_id) REFERENCES jobs(job_id)
)
""")

# Create `friends` table
cur.execute("""
DROP TABLE IF EXISTS `friends`;
""")
cur.execute("""
CREATE TABLE `friends` (
  `friend_id` INTEGER PRIMARY KEY NOT NULL,
  `friend_from_user_id` INTEGER NOT NULL,
  `friend_to_user_id` INTEGER NOT NULL,
  `friend_is_invite` INTEGER NOT NULL,
  FOREIGN KEY(friend_from_user_id) REFERENCES users(user_id),
  FOREIGN KEY(friend_to_user_id) REFERENCES users(user_id)
)
""")
# Create `profiles` table
cur.execute("""
DROP TABLE IF EXISTS `profiles`;
""")
cur.execute("""
CREATE TABLE `profiles` (
  `profile_id` INTEGER PRIMARY KEY NOT NULL,
  `profile_title` varchar(32),
  `profile_description` varchar(512),
  `profile_user_id` INTEGER NOT NULL,
  FOREIGN KEY(profile_user_id) REFERENCES users(user_id)
)
""")
# Create `experiences` table
cur.execute("""
DROP TABLE IF EXISTS `experiences`;
""")
cur.execute("""
CREATE TABLE `experiences` (
  `experience_id` INTEGER PRIMARY KEY NOT NULL,
  `experience_title` varchar(64),
  `experience_employer` varchar(64),
  `experience_date_started` varchar(32),
  `experience_dete_ended` varchar(32),
  `experience_location` varchar(64),
  `experience_description` varchar(512),
  `experience_profile_id` INTEGER NOT NULL,
  FOREIGN KEY(experience_profile_id) REFERENCES profiles(profile_id)
)
""")
cur.execute("""
DROP TABLE IF EXISTS `educations`;
""")
cur.execute("""CREATE TABLE `educations` (
  `education_id` INTEGER PRIMARY KEY NOT NULL,
  `edu_schoolName` varchar(64),
  `edu_degree` varchar(64),
  `edu_startingYear` varchar(32),
  `edu_endingYear` varchar(32),
  `education_profile_Id` INTEGER NOT NULL,
  FOREIGN KEY(education_profile_id) REFERENCES profiles(profile_id)
)
""")

cur.execute("""
DROP TABLE IF EXISTS `messages`;
""")
cur.execute("""CREATE TABLE `messages` (
  `message_id` INTEGER PRIMARY KEY NOT NULL,
  `from_user_id` varchar(64),
  `to_user_id` varchar(64),
  `message` varchar(512),
  FOREIGN KEY(from_user_id) REFERENCES users(user_id),
  FOREIGN KEY(to_user_id) REFERENCES users(user_id)
)
""")
