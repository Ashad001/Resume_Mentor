# Resume Mentor

Resume Mentor is a user-friendly project designed to assist individuals in enhancing their resumes. Crafting a compelling resume can be challenging, and Resume Mentor aims to simplify the process by providing valuable guidance and tips. Whether you're a recent graduate or a seasoned professional, this application offers personalized advice to showcase your skills and accomplishments effectively.


## Prerequisites

Before you begin, ensure you have the following prerequisites installed:

- Docker: [Install Docker](https://docs.docker.com/get-docker/)

## Getting Started

Follow these steps to set up and run the Flask app using Docker:

1. **Clone the Repository:**

    ```bash
    git clone <repository_url>
    cd <Resume_Mentor>
    ```

2. **Build the Docker Image:**

    Build the Docker image using the provided Dockerfile. Run this command from the root of the project directory:

    ```bash
    docker build -t resume-mentor .
    ```

3. **Run the Docker Container:**

    After the image is built, you can run the Docker container with the following command:

    ```bash
    docker run -p 8000:8000 resume-mentor
    ```

    The Flask app will be accessible at `http://localhost:8000` in your web browser.

4. **Stopping the App:**

    To stop the running Docker container, press `Ctrl + C` in the terminal where the container is running.

## Project Structure

The project directory is structured as follows:

```
resume-mentor/
├── requirements.txt
├── src/
│   ├── main.py
|   ├── __init__.py  
├── Dockerfile
├── setup.py
└── README.md
```

- `requirements.txt`: Lists the Python dependencies required for the app.
- `src/`: Contains the source code for the app.
- `src/main.py`: Defines the app and its routes.
- `Dockerfile`: Defines the Docker image setup and instructions for building the image.
- `README.md`:  Provides instructions for setting up and running the project.
