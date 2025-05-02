# 📚 LendingFront Loan Application - Backend

This project is the backend server for a small business loan application simulation. It was developed following Flask's Factory pattern to easily adapt to both development and production environments.

It was built as part of a technical assessment.

## 📄 Table of Contents

- [🚀Quickstart](#🚀quickstart)
    - [🔍Prerequisites](#🔍prerequisites)
    - [📦Dependencies](#📦dependencies)
    - [💻Development](#💻development)
    - [🧪Testing](#🧪testing)
        - [🧰Setup](#🧰setup)
        - [▶️Run Tests](#▶️run-tests)
- [🌐Production](#🌐production)
    - [⚙️Railway Configuration](#⚙️railway-configuration)
    - [🛠Steps to Deploy on Railway](#🛠steps-to-deploy-on-railway)
- [🔧Built With](#🔧built-with)
- [👥Authors](#👥authors)
- [📜License](#📜license)

# 🚀Quickstart

## 🔍Prerequisites

Before you begin configuring and running this project, make sure you have the following components installed on your system:

1. **Git**: To clone the repository and collaborate in development.

2. **Python and pip**: Required to develop and run the Flask application and Python's package installer, necessary to install project dependencies.

3. **venv (recommended)**: To create an isolated Python environment for dependency management.

## 📦Dependencies

This project uses the following technologies and versions:

- **Python**: = 3.10.12
- **Flask**: = 3.1.0

Please keep these versions in mind when setting up your development environment.

## 💻Development

Describe how to install all development dependencies and run the application.

1. Clone this repository to your local machine.
2. Open a terminal in the project folder.
3. Create and activate a virtual environment:
```bash
    python3 -m venv venv
    source venv/bin/activate  # Linux/Mac
    venv\Scripts\activate     # Windows
```
4. Install the project dependencies:
```bash
    pip install -r requirements.txt
```
5. Start the development server `python3 main.py`

Remember to create the environment variables before starting the project following the example `.env.template` in the repository.

## 🧪Testing

This project includes unit tests written using [`pytest`](https://docs.pytest.org/)

### 🧰Setup

Follow these steps to prepare and run the test suite:

1. Make sure you are in the root of the project directory.
2. Activate your virtual environment:

```bash
    source venv/bin/activate  # On Linux/macOS
    venv\Scripts\activate      # On Windows
```

### ▶️Run Tests

To run the tests using `pytest`, use the following commands:

- Run all tests in the project:

```bash
    pytest
```

# 🌐Production

This application is deployed using [Railway](https://railway.app), a cloud platform that simplifies backend deployments.

## ⚙️Railway Configuration

The project includes a `railway.json` configuration file that instructs Railway how to build and run the app in production. The relevant settings are:

```json
{
  "$schema": "https://railway.app/railway.schema.json",
  "build": {
    "builder": "NIXPACKS"
  },
  "deploy": {
    "startCommand": "gunicorn wsgi:app",
    "restartPolicyType": "ON_FAILURE",
    "restartPolicyMaxRetries": 10
  }
}
```
## 🛠Steps to Deploy on Railway

1. **Connect the repository**  
   - Go to [Railway](https://railway.app) and log in.  
   - Click **"New Project" → "Deploy from GitHub Repo"**.  
   - Select this repository to import.

2. **Environment Variables**  
   - Navigate to the **"Variables"** tab.  
   - Add all environment variables as defined in the `.env.template` file.

3. **Deployment Command**  
   - The application uses **Gunicorn** to run the Flask app.  
   - The startup command is already set in `railway.json`:
     ```bash
     gunicorn wsgi:app
     ```

4. **Automatic Deploys**  
   - Railway will automatically redeploy the project whenever you push changes to the `main` branch.

# 🔧Built With

* [Python](https://www.python.org/)
* [Flask](https://flask.palletsprojects.com/en/stable/)

# 👥Authors

* **Efraín González** - *Software Developer*

# 📜License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.