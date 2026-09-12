# AI/ML Trainee Assessment

**Candidate:** Mohd Zaid  
**Position:** AI/ML Trainee  
**Assessment:** AccuKnox AI/ML Trainee Assessment  
**Date:** September 2026

---

## Overview

This repository contains my solutions for the **AccuKnox AI/ML Trainee Assessment**.

The assessment covers practical implementation of Python, REST APIs, SQLite, CSV data processing, data visualization, LLM concepts, AI/ML concepts, agentic chatbot architecture, and vector databases.

---

## Repository Structure

```text
AI-ML-Trainee-Assessment/
│
├── API Data Retrieval and Storage.py
├── CSV Data Import to a Database.py
├── Data Processing and Visualization.py
├── README.md
└── requirements.txt
```

---

# Assignment 1

## 1. API Data Retrieval and Storage

### Objective

Fetch book information from an external REST API, store the required data in a local SQLite database, and display the stored records.

### API Used

**Open Library Search API**

The following information is extracted from the API response:

- Book title
- Author
- First publication year

### Database Schema

The SQLite database contains a `books` table with the following columns:

| Column | Type | Description |
|---|---|---|
| `id` | INTEGER | Primary key with auto-increment |
| `title` | TEXT | Book title |
| `author` | TEXT | Author name |
| `publication_year` | INTEGER | First publication year |

A `UNIQUE(title, publication_year)` constraint is used to prevent duplicate book records based on the selected uniqueness assumption.

### Approach

1. Connect to the SQLite database.
2. Create the `books` table if it does not exist.
3. Send a GET request to the Open Library API.
4. Validate the API response.
5. Extract the required book information.
6. Handle records where the publication year is unavailable.
7. Insert the records into SQLite.
8. Commit the transaction.
9. Retrieve and display the stored records.
10. Close the database connection.

### Key Concepts

- Python
- REST API
- Requests
- JSON
- SQLite
- SQL
- Parameterized SQL queries
- Database constraints
- Error handling

---

## 2. Data Processing and Visualization

### Objective

Fetch student score data from an external API, calculate the average score for each student, calculate the overall average, and visualize the results using a bar chart.

### Subjects

The following subjects are processed:

- Mathematics
- History
- Physics
- Chemistry
- Biology
- English
- Geography

### Average Calculation

For each student:

```text
Average = Sum of valid subject scores / Number of valid subject scores
```

Only numeric score values are included in the calculation.

### Approach

1. Fetch student data from the provided REST API.
2. Validate the API response.
3. Extract valid numeric subject scores.
4. Calculate the average for each student.
5. Calculate the overall average.
6. Display the student averages.
7. Generate a bar chart using Matplotlib.
8. Save the chart as `student_scores.png`.

### Key Concepts

- Python
- REST API
- Requests
- JSON processing
- Data validation
- Mathematical calculations
- Matplotlib
- Data visualization

---

## 3. CSV Data Import to a Database

### Objective

Read user information from a CSV file and insert the records into a local SQLite database.

### Input Data

The CSV file contains:

- Name
- Email

### Database Schema

The SQLite database contains a `users` table:

| Column | Type | Constraint |
|---|---|---|
| `id` | INTEGER | Primary key with auto-increment |
| `name` | TEXT | NOT NULL |
| `email` | TEXT | NOT NULL, UNIQUE |

Email is treated as the unique identifier for a user.

### Approach

1. Read the CSV file using Pandas.
2. Validate the required CSV columns.
3. Remove records with missing name or email.
4. Remove unnecessary whitespace.
5. Create the `users` table if it does not exist.
6. Insert valid records using parameterized SQL queries.
7. Handle duplicate email addresses.
8. Commit the transaction.
9. Display the users stored in the database.

### Key Concepts

- Python
- Pandas
- CSV processing
- SQLite
- SQL
- Data cleaning
- Database constraints
- Duplicate handling

---

# Assignment 2

## 1. Self Assessment

My current self-assessment is:

| Area | Rating |
|---|---|
| LLM | A |
| AI | A |
| ML | B |
| Deep Learning | B |

### Rating Criteria

- **A:** Able to code independently
- **B:** Able to code under supervision
- **C:** Little or no understanding

I selected these ratings based on my current practical experience. My strongest hands-on experience is in **Generative AI and LLM application development**, including LLM-based applications, RAG systems, AI agents, and related frameworks.

---

# 2. High-Level LLM Chatbot Architecture

## Use Case

The proposed architecture is for an **agentic personal expense assistant**.

The chatbot allows users to interact with their expense data using natural language.

Example requests include:

- Add ₹500 for food
- Show my expenses
- Summarize my spending
- Search for information

## Architecture

```text
User
  |
  v
Streamlit UI
  |
  v
Backend
  |
  v
LangGraph Agent Workflow
  |
  v
LLM
  |
  +-------------------+
  |                   |
  v                   v
Tool Calling          MCP
  |                   |
  +---------+---------+
            |
            v
          Tools
        /       \
       v         v
Expense Tools   Web Search
       |
       v
    SQLite
   Database
```

### Components

**Streamlit UI**

Provides the interface through which the user interacts with the chatbot.

**Backend**

Handles application logic and communication between the UI, agent workflow, tools, and data layer.

**LangGraph**

Manages the agentic workflow and controls the flow between the LLM and available tools.

**LLM**

Understands the user's natural-language request and determines the appropriate response or tool to use.

**Tool Calling**

Allows the LLM-powered agent to invoke specific application capabilities.

For example:

| User Request | Possible Tool |
|---|---|
| Add ₹500 for food | `add_expense` |
| Show expenses | `list_expenses` |
| Summarize spending | `summarize` |
| Search information | `web_search` |

**MCP**

Model Context Protocol can provide a structured interface for connecting the AI application with external tools and capabilities.

**SQLite**

Stores expense information and provides the data required for expense-related queries and summaries.

**Web Search**

A web-search capability can be used when the user's request requires external information.

---

# 3. Vector Database

## What is a Vector Database?

A vector database is used to store and retrieve vector representations, known as **embeddings**, of data.

Embeddings represent the semantic meaning of text as numerical vectors. This allows a system to perform semantic similarity search and retrieve information based on meaning rather than only exact keyword matching.

## Example: YouTube Question Answering

A YouTube question-answering system can follow this pipeline:

```text
YouTube Video
      |
      v
Transcript
      |
      v
Text Chunking
      |
      v
Embeddings
      |
      v
FAISS Vector Store
      |
      v
Similarity Search
      |
      v
Relevant Context
      |
      v
LLM
      |
      v
Final Answer
```

### Retrieval Process

1. Obtain the video transcript.
2. Divide the transcript into smaller chunks.
3. Generate embeddings for the chunks.
4. Store the embeddings in FAISS.
5. Convert the user's question into an embedding.
6. Search for semantically similar chunks.
7. Retrieve the most relevant context.
8. Provide the retrieved context to the LLM.
9. Generate the final answer.

### Embedding Model

The example uses:

```text
intfloat/multilingual-e5-large
```

### Why FAISS?

I selected FAISS because:

- It is lightweight.
- It integrates well with Python.
- It provides efficient similarity search.
- It is suitable for a practical local RAG application.
- I have practical experience working with FAISS-based retrieval workflows.

For larger-scale production systems, a managed or distributed vector database could be considered depending on the application's scale and infrastructure requirements.

---

# Technologies Used

| Category | Technologies |
|---|---|
| Programming | Python, SQL |
| API | REST API, Requests |
| Database | SQLite |
| Data Processing | Pandas |
| Visualization | Matplotlib |
| LLM | Hugging Face / Llama |
| LLM Frameworks | LangChain, LangGraph |
| AI Integration | MCP, Tool Calling |
| Embeddings | Hugging Face Embeddings |
| Vector Search | FAISS |
| UI / Backend | Streamlit, FastAPI |
| Version Control | Git, GitHub |

---

# Assumptions

The following assumptions were made during the assessment:

1. For the books dataset, the combination of book title and first publication year is sufficient for identifying duplicate records.
2. Books without a first publication year are skipped because the publication year is part of the database uniqueness logic.
3. For the user dataset, email is treated as a unique identifier.
4. Only valid numeric student scores are included when calculating averages.
5. The chatbot architecture is a high-level design demonstrating the interaction between the user, LLM, agent workflow, tools, and data sources.
6. FAISS is considered suitable for the hypothetical YouTube RAG use case. Larger-scale applications may require a different vector database architecture.

---

# How to Run

## 1. Clone the Repository

```bash
git clone <your-github-repository-url>
cd AI-ML-Trainee-Assessment
```

## 2. Create a Virtual Environment

```bash
python -m venv venv
```

### Windows

```bash
venv\Scripts\activate
```

## 3. Install Dependencies

```bash
pip install -r requirements.txt
```

## 4. Run the Programs

### API Data Retrieval and Storage

```bash
python "API Data Retrieval and Storage.py"
```

### Data Processing and Visualization

```bash
python "Data Processing and Visualization.py"
```

### CSV Data Import to a Database

```bash
python "CSV Data Import to a Database.py"
```

---

# Error Handling

The implementations include handling for common situations such as:

- HTTP request failures
- Unexpected API responses
- Missing data
- Non-numeric student scores
- Missing CSV columns
- Empty CSV files
- Duplicate email addresses
- Database errors
- Missing publication years

The implementations aim to remain simple and readable while handling common data and runtime issues.

---

# Conclusion

This repository demonstrates my practical understanding of:

- Python
- REST APIs
- SQL and SQLite
- Data processing
- Data visualization
- LLM applications
- Agentic AI
- Tool calling
- MCP
- RAG
- Embeddings
- Vector search

Thank you for reviewing my submission.

**Mohd Zaid**  
AI/ML Trainee Candidate