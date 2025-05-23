# Climate Dashboard Application

This project is a web application built using Dash, Plotly, and Pandas to visualize climate data trends. The application allows users to explore global climate indicators and compare them between the Northern and Southern Hemispheres.

## Project Structure

```
climate-dashboard-app
├── app
│   ├── __init__.py
│   ├── final_dashboard_with_ui_upgrade.py
│   └── assets
├── requirements.txt
└── README.md
```

## Installation

To set up the project, follow these steps:

1. Clone the repository:
   ```
   git clone <repository-url>
   cd climate-dashboard-app
   ```

2. Create a virtual environment (optional but recommended):
   ```
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. Install the required packages:
   ```
   pip install -r requirements.txt
   ```

## Running the Application

To run the Dash application, execute the following command in your terminal:

```
python app/final_dashboard_with_ui_upgrade.py
```

Once the server is running, open your web browser and navigate to `http://127.0.0.1:8050` to view the application.

## Deployment

To share the application online, you can deploy it using platforms like Heroku, Dash Deployment Server, or Render. Follow the specific deployment instructions for your chosen platform, which typically involve:

- Creating a `Procfile` to specify how to run your application.
- Setting environment variables as needed.
- Pushing your code to the platform's repository.

## Features

- Interactive visualizations of climate data trends.
- Comparison of climate indicators between the Northern and Southern Hemispheres.
- Options to export filtered data as CSV.

## Requirements

The application requires the following Python packages:

- Dash
- Plotly
- Pandas
- NumPy

Make sure to install all dependencies listed in `requirements.txt`.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.