# Dataset Setup — EduTrack LMS

## 1. Client Datasets

The project uses the following three datasets supplied in the client brief.

| Dataset | Purpose |
|---|---|
| `aiml_student_performance.csv` | Inspect student performance information |
| `aiml_content_engagement.csv` | Identify student-course interactions and engagement signals |
| `aiml_edtech_tests.json` | Inspect the test data and determine its role |

## 2. Dataset Sources

- Student performance: https://cynarissolutions.com/candidate/client-project-pack/aiml-edtech/aiml_student_performance.csv
- Content engagement: https://cynarissolutions.com/candidate/client-project-pack/aiml-edtech/aiml_content_engagement.csv
- EdTech tests: https://cynarissolutions.com/candidate/client-project-pack/aiml-edtech/aiml_edtech_tests.json

## 3. Expected Local Structure

```text
data/
├── README.md
├── aiml_student_performance.csv
├── aiml_content_engagement.csv
└── aiml_edtech_tests.json
```

Download the three supplied datasets and place them in the local `data/` directory. The Python pipeline will inspect the files before preprocessing or training.

## 4. Data Inspection

The Python pipeline will check:

- File availability and readability.
- Column names and data types.
- Number of rows and columns.
- Missing values and duplicate records.
- Student and course identifiers.
- Available engagement and performance fields.

The results will guide the preprocessing strategy and recommendation model selection.

## 5. Data Handling

- Keep credentials and API keys out of the repository.
- Do not commit sensitive student information.
- Use the supplied datasets for the project and follow applicable data-protection requirements.

## 6. Current Status

Dataset sources are documented. Dataset inspection and validation will be implemented in Python.
