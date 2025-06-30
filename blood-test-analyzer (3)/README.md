# Blood Test Report Analyzer

A comprehensive AI-powered blood test report analysis system using CrewAI, FastAPI, and multiple specialized AI agents.

## 🩺 Features

- **Multi-Agent Analysis**: Specialized AI agents for medical analysis, nutrition recommendations, and exercise planning
- **Document Verification**: Validates uploaded blood test reports
- **Comprehensive Reports**: Detailed analysis with actionable recommendations
- **RESTful API**: Easy integration with web applications
- **Multiple Analysis Types**: Choose from comprehensive, nutrition-focused, exercise-focused, or verification-only analysis

## 🏗️ Project Structure

\`\`\`
blood-test-analyzer/
├── data/                    # Temporary file storage
├── scripts/                 # Test and utility scripts
│   ├── test_api.py         # Automated API testing
│   ├── manual_test.py      # Manual PDF upload testing
│   └── create_sample_data.py # Generate sample blood test PDFs
├── .env                    # Environment variables
├── requirements.txt        # Python dependencies
├── tools.py               # Custom CrewAI tools
├── agents.py              # AI agent definitions
├── task.py                # Task definitions for agents
├── main.py                # FastAPI application
└── README.md              # This file
\`\`\`

## 🚀 Quick Start

### 1. Clone and Setup
\`\`\`bash
git clone <your-repo>
cd blood-test-analyzer
python -m venv venv

# Activate virtual environment
# Windows:
venv\Scripts\activate
# macOS/Linux:
source venv/bin/activate
\`\`\`

### 2. Install Dependencies
\`\`\`bash
pip install -r requirements.txt
\`\`\`

### 3. Configure Environment
Create a `.env` file:
\`\`\`env
OPENAI_API_KEY=your_openai_api_key_here
SERPER_API_KEY=your_serper_api_key_here  # Optional
PYTHONPATH=.
\`\`\`

### 4. Run the Application
\`\`\`bash
python main.py
\`\`\`

The API will be available at `http://localhost:8000`

## 🔧 API Endpoints

### Health Check
- **GET** `/` - Basic health check
- **GET** `/health` - Detailed health status

### Blood Test Analysis
- **POST** `/analyze` - Upload and analyze blood test reports

#### Parameters:
- `file` (required): PDF file containing the blood test report
- `query` (optional): Specific question about the blood test
- `analysis_type` (optional): Type of analysis
  - `comprehensive` (default): Full analysis with all specialists
  - `nutrition`: Focus on nutrition recommendations
  - `exercise`: Focus on exercise planning
  - `verification`: Document verification only

#### Example Usage:
\`\`\`bash
curl -X POST "http://localhost:8000/analyze" \
  -F "file=@blood_test.pdf" \
  -F "query=What do my cholesterol levels mean?" \
  -F "analysis_type=comprehensive"
\`\`\`

## 🧪 Testing

### Automated Testing
\`\`\`bash
python scripts/test_api.py
\`\`\`

### Manual Testing with Your PDF
\`\`\`bash
python scripts/manual_test.py
\`\`\`

### Create Sample Data
\`\`\`bash
python scripts/create_sample_data.py
\`\`\`

## 🤖 AI Agents

1. **Doctor Agent**: Senior medical professional for blood test interpretation
2. **Nutritionist Agent**: Clinical nutritionist for dietary recommendations
3. **Exercise Specialist**: Clinical exercise physiologist for fitness planning
4. **Verifier Agent**: Medical document verification specialist

## 📊 Sample Output

### Comprehensive Analysis
\`\`\`json
{
  "status": "success",
  "query": "Analyze my blood test results",
  "analysis_type": "comprehensive",
  "analysis": "BLOOD TEST ANALYSIS REPORT\n\nSUMMARY OF KEY FINDINGS:\n• Glucose Level: 95 mg/dL - Within normal range...",
  "file_processed": "blood_test.pdf",
  "disclaimer": "This analysis is for informational purposes only..."
}
\`\`\`

## 🔒 Important Notes

- This system is for **informational purposes only**
- Always consult healthcare professionals for medical decisions
- Uploaded files are automatically deleted after processing
- Ensure your OpenAI API key has sufficient credits

## 🛠️ Development

### Adding New Agents
1. Define agent in `agents.py`
2. Create corresponding tasks in `task.py`
3. Update the crew configuration in `main.py`

### Adding New Tools
1. Create tool class in `tools.py`
2. Import and assign to relevant agents
3. Update task descriptions to utilize new tools

## 📝 Environment Variables

| Variable | Description | Required |
|----------|-------------|----------|
| `OPENAI_API_KEY` | OpenAI API key for LLM | Yes |
| `SERPER_API_KEY` | Serper API key for web search | No |
| `PYTHONPATH` | Python path configuration | Yes |

## 🐛 Troubleshooting

### Common Issues:

1. **Import Errors**: Ensure all dependencies are installed
   \`\`\`bash
   pip install --upgrade crewai fastapi langchain-openai
   \`\`\`

2. **API Key Errors**: Verify your OpenAI API key is set correctly
   \`\`\`bash
   python -c "import os; from dotenv import load_dotenv; load_dotenv(); print(os.getenv('OPENAI_API_KEY'))"
   \`\`\`

3. **Port Issues**: Change port in `main.py` if 8000 is busy
   ```python
   uvicorn.run(app, host="0.0.0.0", port=8001, reload=True)
   \`\`\`

4. **PDF Processing Issues**: Ensure PDFs are valid and not corrupted

### Debug Mode
Set `verbose=True` in agent configurations for detailed logging.

## 📄 License

This project is for educational and research purposes. Please ensure compliance with medical data regulations in your jurisdiction.

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Test thoroughly
5. Submit a pull request

## 📞 Support

For issues and questions:
1. Check the troubleshooting section
2. Review the API documentation at `http://localhost:8000/docs`
3. Create an issue in the repository

---

**Disclaimer**: This tool provides informational analysis only and should not replace professional medical consultation.
