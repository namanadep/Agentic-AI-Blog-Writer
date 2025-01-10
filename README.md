# Blog Content Generator

This project is a Blog Content Generator that uses AI agents to research and write blog posts based on a given topic. The application is built using Streamlit for the user interface and CrewAI for managing the AI agents.

## Features

- **User Input**: Enter a topic for the blog post.
- **AI Agents**: Two AI agents, a Blog Researcher and a Blog Writer, work together to generate the blog content.
- **YouTube Integration**: The Blog Researcher uses a YouTube search tool to gather information from a specified YouTube channel.
- **Sequential Task Execution**: The tasks are executed sequentially to ensure a coherent workflow.

## Project Structure

- `app.py`: Main application file for the Streamlit interface.
- `agents.py`: Defines the AI agents used in the project.
- `crew.py`: Configures the CrewAI setup with agents and tasks.
- `tasks.py`: Defines the tasks for the AI agents.
- `tools.py`: Contains the YouTube search tool configuration.
- `db/`: Directory for database files.
- `requirements.txt`: Lists the Python dependencies.
- `.env`: Environment variables file (contains API keys).

## Installation

1. Clone the repository:
    ```sh
    git clone <repository-url>
    cd <repository-directory>
    ```

2. Create a virtual environment and activate it:
    ```sh
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. Install the dependencies:
    ```sh
    pip install -r requirements.txt
    ```

4. Set up the environment variables in the [.env](http://_vscodecontentref_/9) file:
    ```env
    OPENAI_API_KEY="your-openai-api-key"
    ```

## Usage

1. Run the Streamlit application:
    ```sh
    streamlit run app.py
    ```

2. Enter a topic for the blog post in the Streamlit interface and click "Generate Blog".

## License

This project is licensed under the MIT License.
