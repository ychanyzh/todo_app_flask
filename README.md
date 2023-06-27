# Todo List Website

This is a simple todo list website built using Flask, a Python web framework. The website allows users to add tasks with titles and descriptions, view the list of tasks, and delete tasks.

## Prerequisites

Make sure you have the following installed on your machine:

- Python (version 3.x)
- Flask (can be installed via `pip install flask`)

## Getting Started

1. Clone the repository or download the project files to your local machine.

2. Open a terminal and navigate to the project directory.

3. Set up a virtual environment (optional but recommended):
   - Run `virtualenv flask` to create a new virtual environment.
   - Activate the virtual environment:
     - For Linux/Mac: `source bin/activate`
     - For Windows: `Scripts\activate`

4. Install the required dependencies by running `pip install -r requirements.txt`.

5. Create the SQLite database:
   - Run `python init_db.py` to create the database file (`todo.db`) and initialize the tasks table.

6. Start the application:
   - Run `python app.py`.
   - The Flask development server will start running locally.

7. Open a web browser and visit `http://localhost:5000` or `http://127.0.0.1:5000/` to access the website.

## Project Structure

- `app.py`: Main entry point of the Flask application.
- `init_db.py`: Script to create the SQLite database and initialize the tasks table.
- `templates/`: Directory containing HTML templates used to render web pages.
- `static/`: Directory containing static files such as CSS and JavaScript.

## Contributing

Contributions are welcome! If you have any suggestions, bug reports, or feature requests, please open an issue or submit a pull request.

## License

This project is licensed under the [MIT License](LICENSE).
