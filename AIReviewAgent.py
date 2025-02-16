import requests
import sys
from fpdf import FPDF
import os

#  Set Up API Credentials:
#Replace ENTER_HUGGINGFACE_KEY_HERE with hugging face key token generated in the website:
#I have not put mine since it is a secret key.
API_URL = "https://api-inference.huggingface.co/models/tiiuae/falcon-7b-instruct"
HEADERS = {"Authorization": "Bearer ENTER_HUGGINGFACE_KEY_HERE"}  # Replace with own your Hugging Face API Key

# Function to Generate Text via Falcon-7B:
def generate_text(prompt):
    payload = {
        "inputs": prompt,
        "parameters": {
            "max_length": 700,
            "temperature": 0.7,
            "top_p": 0.9
        }
    }

    response = requests.post(API_URL, headers=HEADERS, json=payload)
    response_json = response.json()

    try:
        generated_text = response_json[0]["generated_text"]
        return generated_text.strip()
    except Exception as e:
        print(f"Error: {e}")
        return None

#  Get User Input for Press Release
def get_user_input():
#Company info:
    company_name = input("Enter the company name: ")
    flagship_product = input("Enter the flagship Product/Service: ")
    achievements = input("Enter the major achievements: ")
#Press kit info:
    press_topic = input("Enter the press kit topic: ")
    target_media = input("Enter the target media (e.g., Business, Tech, General): ")
    tone = input("Enter the tone (e.g., Professional, Formal, Creative): ")
   
    return f""" Write a professional press release for {company_name} launching {press_topic}.
    Target audience: {target_media}.
    Tone: {tone}.

    Key highlights:
    - Flagship Product: {flagship_product}
    - Major Achievements: {achievements}

    Provide a compelling introduction, detailed body, and a strong conclusion.

    ### Response:"""

#  Generate Press Release
def generate_press_release():
    user_prompt = get_user_input()
    print("\nGenerating Press Release...\n")
    press_release = generate_text(user_prompt)

    if press_release:
        print("\nGenerated Press Release:\n", press_release)
        return press_release
    else:
        print("Error generating text.")
        return None

#  Review Press Kit with Scoring (0-10)
def review_press_kit(text):
    prompt = f"""
    Review the following press release and rate it on a scale of 0-10 based on:
    
    1 **Content Consistency**: (Score: _/10)
    - Explanation:  
    
    2 **Writing Style and Tone**: (Score: _/10)
    - Explanation:  

    3 **Layout and Structure**: (Score: _/10)
    - Explanation:  

    4 **SEO Optimization**: (Score: _/10)
    - Explanation:  

    Provide **both numerical scores (0-10) and detailed feedback**.

    ### Press Release:
    {text}

    ### Review:
    """

    print("\nReviewing Press Release...\n")
    review_text = generate_text(prompt)

    if review_text:
        print("\nReview Report:\n", review_text)
        return review_text
    else:
        print("Error generating review.")
        return None

# Save the Review as a PDF
def save_to_pdf(filename, title, content):
    pdf = FPDF()
    pdf.set_auto_page_break(auto=True, margin=15)
    pdf.add_page()
    
    pdf.set_font("Arial", "B", 16)
    pdf.cell(200, 10, title, ln=True, align="C")
    pdf.ln(10)

    pdf.set_font("Arial", "", 12)
    for line in content.split("\n"):
        pdf.multi_cell(0, 8, line)
        pdf.ln(2)
    # Get full file path
    file_path = os.path.abspath(filename)
    
    pdf.output(file_path)
    print(f"PDF saved at: {file_path}")
    pdf.output(filename)
    print(f"PDF saved successfully as: {filename}")

# Run from CLI
if __name__ == "__main__":
    press_release = generate_press_release()

    if press_release:
        review_report = review_press_kit(press_release)

        if review_report:
            save_to_pdf("press_kit_review.pdf", "Press Kit Review", review_report)
