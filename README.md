# Linux_Final

## Project Description
A simple to-do list web app built with Python/Flask. Supports adding, deleting, and updating tasks via a REST API. Includes a GitHub Actions CI pipeline that automatically runs linting and tests on every push to `main`.

## Requirements
- Python 3.11+
- pip

## Setup & Running

1. **Clone the repository**
   ```bash
   git clone <your-repo-url>
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the app**
   ```bash
   python app.py
   ```

## Running Tests
```bash
pytest test_app.py -v
```

## CI Pipeline
On every push to `main`, GitHub Actions will:
- Run `pylint` on the source files
- Run `pytest` with timing info
- Upload the test log as a downloadable artifact