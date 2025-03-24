from models.llama_model import generate_questions
from models.fetch_answers import search_answer
from models.evaluate_answers import evaluate_answer

def knowledge_assessment(job_role, resume, user_responses):
    """Runs full knowledge assessment pipeline."""
    questions = generate_questions(job_role, resume)
    expected_answers = [search_answer(q) for q in questions]

    scores = [
        evaluate_answer(user_responses[i], expected_answers[i])
        for i in range(len(questions))
    ]
    
    return sum(scores) / len(scores)

if __name__ == "__main__":
    job_role = "Software Engineer"
    resume = "Python developer with experience in AI and web development."
    user_responses = [
        "A neural network has layers that process data.",
        "Recursion is when a function calls itself.",
        "A REST API uses HTTP methods to interact with resources.",
    ]
    
    print("Final Knowledge Score:", knowledge_assessment(job_role, resume, user_responses))
