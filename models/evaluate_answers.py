from sentence_transformers import SentenceTransformer, util
import nltk
from nltk.tokenize import word_tokenize

nltk.download("punkt")
model = SentenceTransformer("sentence-transformers/all-MiniLM-L6-v2")

def extract_keywords(text):
    """Extracts key words from text."""
    words = word_tokenize(text.lower())
    words = [word for word in words if word.isalnum()]
    return set(words)

def evaluate_answer(user_answer, expected_answer):
    """Compares user answer with expected answer and assigns a knowledge score."""
    user_keywords = extract_keywords(user_answer)
    expected_keywords = extract_keywords(expected_answer)
    
    common_keywords = user_keywords.intersection(expected_keywords)
    keyword_score = len(common_keywords) / max(len(expected_keywords), 1)
    
    similarity_score = util.pytorch_cos_sim(
        model.encode(user_answer, convert_to_tensor=True),
        model.encode(expected_answer, convert_to_tensor=True)
    ).item()
    
    final_score = round((keyword_score * 0.5 + similarity_score * 0.5) * 10, 2)
    return final_score

if __name__ == "__main__":
    print(evaluate_answer("A neural network has layers that process data.", 
                          "A neural network consists of layers of neurons that process input data."))
