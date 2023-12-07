# Birthday Wisher

Birthday Wisher is a Python script that checks for birthdays in a CSV file, selects a random letter template, and sends a birthday email to the celebrant.

## Requirements

- Python 3.x
- Pandas library (`pip install pandas`)
- smtplib library (built-in with Python)

## Usage

1. **Clone the repository:**

    ```bash
    git clone https://github.com/your-username/birthday-wisher.git
    ```

2. **Navigate to the project directory:**

    ```bash
    cd birthday-wisher
    ```

3. **Install the required libraries:**

    ```bash
    pip install pandas
    ```

4. **Replace your Gmail credentials in the script (`my_email` and `my_password`).**

5. **Prepare your CSV file (`birthdays.csv`) with columns: `name`, `email`, `month`, and `day`.**

6. **Add letter templates in the `Letter templates` directory as text files.**

7. **For the password:**
   - Go to your Gmail settings and enable 2-step verification.
   - Find the "App Passwords" section and add a new app (name it as "birthday wish").
   - Copy the generated code and paste it in `my_password` (remove spaces).

8. **Run the script:**

    ```bash
    python birthday_wisher.py
    ```

## File Structure

birthday-wisher/
│
├── birthday_wisher.py
├── birthdays.csv
├── Letter templates/
│ ├── letter1.txt
│ ├── letter2.txt
│ └── ...
└── README.md


## Note

- The script checks for birthdays based on the current date and sends emails accordingly.
- Ensure that "Allow less secure apps" is turned on for the Gmail account you use for sending emails.

## Auto Run (Optional)

To automate the script, you can use platforms like [PythonAnywhere](https://www.pythonanywhere.com/):
- Note that PythonAnywhere operates in UTC time.
- Keep in mind that PythonAnywhere has an expiration date for free accounts.

Feel free to customize the script, add more letter templates, or improve its functionality according to your needs.
