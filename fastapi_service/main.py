from fastapi import FastAPI
from groq import Groq
from dotenv import load_dotenv
import os
from pydantic import BaseModel
load_dotenv()

client = Groq(
    api_key=os.getenv("GROQ_API_KEY")
)

app = FastAPI()


@app.get("/")
def home():

    return {
        "message": "SkillForge AI FastAPI Service Running"
    }


@app.get("/generate-question/{category}")
def generate_question(category: str):

    prompts = {

       "Python Developer":
"""
Generate 10 short Python developer interview questions.

Rules:
- Focus on Python fundamentals, OOP, functions, APIs, exceptions
- Only questions
- No answers
- No explanations
- Keep questions short
- Do not use markdown
""",

"Django Developer":
"""
Generate 10 short Django interview questions.

Rules:
- Focus on models, views, ORM, authentication, middleware, APIs
- Only questions
- No answers
- No explanations
- Keep questions short
- Do not use markdown
""",

"Frontend Developer":
"""
Generate 10 short frontend developer interview questions.

Rules:
- Focus on HTML, CSS, JavaScript, DOM, responsive design
- Only questions
- No answers
- No explanations
- Keep questions short
- Do not use markdown
""",

"HR Interview":
"""
Generate 10 short HR interview questions.

Rules:
- Focus on communication, teamwork, strengths, weaknesses
- Only questions
- No answers
- No explanations
- Keep questions short
- Do not use markdown
"""
    }

    prompt = prompts.get(category)

    try:

        response = client.chat.completions.create(

            model="llama-3.1-8b-instant",

            messages=[
                {
                    "role": "user",
                    "content": prompt
                }
            ]

        )

        text = response.choices[0].message.content

        questions = text.split("\n")

        cleaned_questions = []

        for q in questions:

            q = q.strip()

            if q:
                q = q.lstrip("1234567890.- ")

                cleaned_questions.append(q)

        return {
            "questions": cleaned_questions
        }

    except Exception as e:

        return {
            "error": str(e)
        }
@app.post("/evaluate-interview")
def evaluate_interview(data: dict):

    questions = data.get("questions")
    answers = data.get("answers")

    results = []

    score = 0

    for question, answer in zip(questions, answers):

        if not answer.strip():

            results.append({

                "question": question,

                "answer": "No answer submitted",

                "evaluation": "Correct: No\nIdeal Answer: Answer was not provided.",

                "correct": False

        })

            continue
        evaluation_prompt = f"""
You are an AI technical interviewer.

Interview Question:
{question}

Candidate Answer:
{answer}

Evaluate the answer strictly.

Rules:
- Decide if answer is correct or wrong
- Give short ideal answer
- Keep response short

Return EXACTLY in this format:

Correct: Yes or No
Ideal Answer: <answer>
"""

        response = client.chat.completions.create(

            model="llama-3.1-8b-instant",

            messages=[
                {
                    "role": "user",
                    "content": evaluation_prompt
                }
            ]
        )

        result_text = response.choices[0].message.content

        is_correct = result_text.lower().startswith("correct: yes")

        if is_correct:
            score += 1

        results.append({
            "question": question,
            "answer": answer,
            "evaluation": result_text,
            "correct": is_correct
        })

    performance = "Needs Improvement"

    if score >= 5:
        performance = "Average"

    if score >= 8:
        performance = "Excellent"

    return {
        "score": score,
        "performance": performance,
        "results": results
    }    
class ChatRequest(BaseModel):

    message: str


@app.post("/chatbot")
def chatbot(data: ChatRequest):

    message = data.message

    prompt = f"""
    You are SkillForge AI assistant.

    Help users learn:
    - Python
    - Django
    - Frontend Development
    - Interview Preparation

Rules:
- Keep answers beginner friendly
- Use simple English
- Keep answers concise
- Use proper spacing
- Use bullet points only when necessary
- Each bullet point must be on a new line
- Avoid long paragraphs
- Do NOT use markdown
- Do NOT use **
- Do NOT use headings
- Format answers cleanly

    User Question:
    {message}
    """

    try:

        response = client.chat.completions.create(

            model="llama-3.1-8b-instant",

            messages=[
                {
                    "role": "user",
                    "content": prompt
                }
            ]

        )

        bot_response = response.choices[0].message.content

        return {
            "response": bot_response
        }

    except Exception as e:

        return {
            "error": str(e)
        }
@app.post("/resume-interview")
def resume_interview(data: dict):

    resume_text = data.get("resume_text")

    prompt = f"""
    Generate interview questions from this resume.

    Rules:

    Return exactly in this format:

    SECTION: Skills-Based Questions

    Question 1
    Question 2
    Question 3

    SECTION: Project-Based Questions

    Question 4
    Question 5
    Question 6

    SECTION: Experience-Based Questions

    Question 7
    Question 8

    SECTION: Personalized Questions For You

    Question 9
    Question 10

    Only questions.
    No introductions.
    No explanations.
    No markdown.
    """

    try:

        response = client.chat.completions.create(

            model="llama-3.1-8b-instant",

            messages=[
                {
                    "role": "user",
                    "content": prompt
                }
            ]

        )

        text = response.choices[0].message.content

        questions = text.split("\n")

        cleaned_questions = []

        for q in questions:

            q = q.strip()

            if q:

                q = q.lstrip("1234567890.- ")

                cleaned_questions.append(q)

        return {

            "questions": cleaned_questions

        }

    except Exception as e:

        return {

            "error": str(e)

        }