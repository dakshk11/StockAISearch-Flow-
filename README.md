# StockAISearch-Flow-
A Streamlit-based web application that integrates with the Firecrawl API to search for stock prices and news, and includes REST API interactions (GET and POST) using JSONPlaceholder for demonstration purposes.

## Overview

The **Stocker** app provides a user-friendly interface to:
- Search for stock prices and the latest news using the Firecrawl API.
- Fetch sample posts via a GET request from JSONPlaceholder.
- Create new posts via a POST request to JSONPlaceholder.

The application is split into two Python files for modularity:
- `ui.py`: Handles the Streamlit user interface and logic.
- `backend.py`: Contains the API interaction functions.

## Features
- Interactive sidebar navigation for different actions.
- Secure API key input with session persistence.
- Real-time feedback with loading spinners and error handling.
- Display of search results in expandable markdown sections.
- JSON response visualization for GET and POST operations.

## Prerequisites
- Python 3.8 or higher.
- Internet connection (required for API calls).

## Installation

1. **Clone the Repository**
   ```bash
   git clone https://github.com/your-username/stocker.git
   cd stocker
   ```

2. **Install Dependencies**
   Create a virtual environment (optional but recommended):
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```
   Install the required packages using the provided `requirements.txt`:
   ```bash
   pip install -r requirements.txt
   ```

3. **Obtain API Key**
   - Sign up at [Firecrawl](https://www.firecrawl.dev/) to get a Firecrawl API key.
   - The app uses JSONPlaceholder (a free fake API) for GET and POST examples, so no additional key is needed for those.

## Usage

1. **Run the Application**
   ```bash
   streamlit run ui.py
   ```

2. **Interact with the App**
   - Enter your Firecrawl API key when prompted.
   - Use the sidebar to select an action:
     - **Search Stocks**: Enter a company name (e.g., "Apple") and token (e.g., "AAPL") to search for stock price and news.
     - **Fetch Posts (GET)**: Enter a post ID (or leave blank for all posts) to fetch from JSONPlaceholder.
     - **Create Post (POST)**: Fill out the form with a title, body, and user ID to create a new post.
   - View the results, which include markdown content for searches and JSON data for API responses.

## File Structure
- `ui.py`: Streamlit UI logic, including input handling and result display.
- `backend.py`: API interaction functions for Firecrawl and JSONPlaceholder.
- `requirements.txt`: List of Python dependencies.
- `README.md`: This file.

## Contributing
1. Fork the repository.
2. Create a new branch (`git checkout -b feature-branch`).
3. Make your changes and commit them (`git commit -m "Add new feature"`).
4. Push to the branch (`git push origin feature-branch`).
5. Open a pull request.

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details (add a `LICENSE` file if desired).

## Acknowledgments
- [Streamlit](https://streamlit.io/) for the web framework.
- [Firecrawl](https://www.firecrawl.dev/) for the web scraping and search API.
- [JSONPlaceholder](https://jsonplaceholder.typicode.com/) for the free REST API service.

## Contact
For questions or issues, please open an issue on the [GitHub repository](https://github.com/your-username/stocker/issues) or contact the maintainer.

---

*Last updated: June 22, 2025*
