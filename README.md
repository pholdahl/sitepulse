# sitepulse

![Project Logo](/img/sitepulsedemo.png)</br>

## Table of Contents

- [About the Project](#about-the-project)
- [Features](#features)
- [Technology Used](#technology-used)
- [Getting Started](#getting-started)
- [Usage](#usage)
- [License](#license)

## About the Project

sitepulse is a simple Python script designed to periodically visit specified websites at regular intervals. This can be particularly useful for keeping free-tier hosting services active, as these often require periodic access to prevent them from going inactive or being decommissioned.

The script is lightweight and can run on your main computer or a separate device, such as a Raspberry Pi, ensuring your hosted services remain live and accessible.

## Features

- **Periodic Website Visits:** Automatically visit a list of websites at user-defined intervals.
- **Error Handling:** Provides feedback on the success of each visit and handles connection errors gracefully.
- **Randomized Interval:** Introduces slight randomization to visit intervals to mimic more natural traffic.
- **Multi-threaded:** Handles multiple websites simultaneously, ensuring efficient use of system resources.

## Technology Used

- **Python 3.x:** The main programming language used for the script.
- **Requests Library:** For handling HTTP requests to the specified websites.
- **Threading Library:** To manage concurrent visits to multiple websites.
- **Time Library:** For managing sleep intervals between visits.
- **Random Library:** To randomize the intervals for visiting websites.

## Getting Started

### Prerequisites

Ensure you have Python 3.x installed on your machine. You can download Python from [python.org](https://www.python.org/downloads/).

### Installation

1. Clone the repository (if applicable):
    ```sh
    git clone https://github.com/yourusername/sitepulse.git
    ```
2. Navigate to the project directory:
    ```sh
    cd sitepulse
    ```
3. Ensure you have the required dependencies installed:
    ```sh
    pip install requests
    ```

### Usage

1. Run the script through the terminal:
    ```sh 
    python3 sitepulse.py
    ```
2. Follow the prompts to input the number of websites, their URLs, 
  and the intervals (in minutes) at which they should be visited.
3. The script will begin visiting each website at the specified intervals, 
  and you will see console output indicating the success or failure of each visit, 
  along with the time until the next visit.
4. The script will continue running indefinitely, keeping your specified websites active.

## License 

This project is licensed under the MIT License.