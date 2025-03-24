from transformers import AutoModelForCausalLM, AutoTokenizer
import torch

# Load LLaMA model
MODEL_NAME = "meta-llama/Llama-2-7b-chat-hf"
tokenizer = AutoTokenizer.from_pretrained(MODEL_NAME)
model = AutoModelForCausalLM.from_pretrained(MODEL_NAME, torch_dtype=torch.float16, device_map="auto")

def generate_questions(job_role, resume):
    """Generate 10 technical interview questions for a given job role."""
    prompt = f"Generate 10 technical interview questions for a {job_role} based on this resume:\n{resume}"
    inputs = tokenizer(prompt, return_tensors="pt").to("cuda")
    outputs = model.generate(**inputs, max_length=500)
    questions = tokenizer.decode(outputs[0], skip_special_tokens=True)
    return questions.split("\n")

if __name__ == "__main__":
    job_role = "Software Engineer"
    resume = "Experienced in Python, AI, and software development."
    print(generate_questions(job_role, resume))
