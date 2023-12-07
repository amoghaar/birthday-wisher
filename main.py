import datetime as dt
import pandas as pd
import os
import random
import smtplib

# Replace with your Gmail credentials
my_email = ""    # type your gmail ID
my_password = ""     # please read the ReadMe file for this

# Read the birthday information from the CSV file into a DataFrame
df = pd.read_csv('birthdays.csv')

# Get the current date and time
current_date = dt.datetime.now()

# Check for rows in the DataFrame where the birthday matches the current date
matching_rows = (df['month'] == current_date.month) & (df['day'] == current_date.day)

# Check if there are any matching birthdays
if matching_rows.any():
    # Select the names of individuals with matching birthdays
    matching_names = df.loc[matching_rows, 'name']

    # Specify the directory containing letter templates
    letter_template_dir = "Letter templates"

    # Get a list of all text files in the letter template directory
    all_files = os.listdir(letter_template_dir)
    txt_files = [file for file in all_files if file.endswith(".txt")]

    # Check if there are any text files in the directory
    if txt_files:
        # Choose a random letter template
        random_letter = random.choice(txt_files)
        letter_path = os.path.join(letter_template_dir, random_letter)

        # Read the content of the chosen letter template
        with open(letter_path, 'r') as letter_file:
            letter_content = letter_file.read()

            # Access the first element of matching_names using .item() to get a string
            new_word = matching_names.item()

            # Replace [NAME] with the actual name in the letter content
            modified_content = letter_content.replace('[NAME]', new_word)

        # Extract the email addresses of individuals with matching birthdays
        receiver_emails = df.loc[matching_rows, 'email']

        # Connect to the SMTP server and send the birthday email
        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(user=my_email, password=my_password)

            # Send the email to each recipient
            for receiver_email in receiver_emails:
                connection.sendmail(
                    from_addr=my_email,
                    to_addrs=receiver_email,
                    msg=f"Subject:Happy Birthday\n\n{modified_content}"
                )

    else:
        print("No letter templates found in the Letter templates directory.")
else:
    print(f"No birthdays found for the current date ({current_date.month}/{current_date.day}).")
