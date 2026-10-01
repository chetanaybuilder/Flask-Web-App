from flask import Blueprint, render_template

main_bp = Blueprint('main', __name__)

@main_bp.route('/')
def home():
    """Render the home portfolio page."""
    portfolio_data = {
        "name": "Chetanay",
        "age": 16,
        "dream": "Europe",
        "skills": ["Python", "HTML", "CSS", "Git", "GitHub", "Artificial Intelligence", "Java", "C++"],
        "projects": [
            {
                "name": "Chatbot",
                "description": "Built using Python and Gemini API"
            },
            {
                "name": "Analyzer Tool for E-commerce",
                "description": "Built using Python and Pandas"
            },
            {
                "name": "Website Development",
                "description": "Built using HTML and CSS"
            }
        ]
    }
    return render_template('index.html', **portfolio_data)
