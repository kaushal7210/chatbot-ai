import requests
import tkinter as tk
from tkinter import scrolledtext, ttk
import tkinter.font as tkFont
from PIL import Image, ImageTk

API_URL = "https://api-inference.huggingface.co/models/deepset/roberta-base-squad2"
headers = {"Authorization": "Bearer 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"}

def query(payload):
    response = requests.post(API_URL, headers=headers, json=payload)
    return response.json()

def get_response():
    question = question_entry.get("1.0", "end").strip()
    context = context_entry.get("1.0", "end").strip()
    output = query({
        "inputs": {
            "question": question,
            "context": context
        },
    })
    response_entry.config(state='normal')
    response_entry.delete("1.0", "end")
    try:
        answer = output['answer']
    except KeyError:
        answer = "No answer found in response. Please check the API response structure"
    
    response_entry.insert("end", answer)
    response_entry.config(state='disabled')

root = tk.Tk()
root.title("TextGenius.Ai by Kaushal Somani")
root.configure(background="peach puff")
root.geometry("1200x900")

font1 = tkFont.Font(family="Elephant", size=16, weight="bold")
font2 = tkFont.Font(family="Rockwell", size=12)

# Create frames
style = ttk.Style()
style.configure("My.TFrame", background="steel blue", borderwidth=5)
left_frame = ttk.Frame(root, width=600, height=900)
left_frame.pack(side="left", pady=20, padx=20, fill="y")

right_frame = ttk.Frame(root, width=600, height=900, style="My.TFrame")
right_frame.pack(side="right", pady=20, padx=20, fill="y")

# Load and display the image
img = Image.open("img3.png")
img = img.resize((600, 800), Image.LANCZOS)
bg_img = ImageTk.PhotoImage(img)
img_label = tk.Label(left_frame, image=bg_img)
img_label.pack()

# Question and Context Section
question_label = tk.Label(right_frame, text="Enter Your Question", font=font1, background="steel blue")
question_label.pack(pady=10)
question_entry = scrolledtext.ScrolledText(right_frame, wrap=tk.WORD, width=50, height=2, font=font2, background="antique white")
question_entry.pack(pady=10)

context_label = tk.Label(right_frame, text="Enter Your Context", font=font1, background="steel blue")
context_label.pack(pady=10)
context_entry = scrolledtext.ScrolledText(right_frame, wrap=tk.WORD, width=50, height=10, font=font2, background="antique white")
context_entry.pack(pady=10)

get_response_button = tk.Button(right_frame, text="Get Response", command=get_response, font=font2, background="peach puff")
get_response_button.pack(pady=10)

response_label = tk.Label(right_frame, text="Answer", font=font1, background="steel blue")
response_label.pack(pady=10)
response_entry = scrolledtext.ScrolledText(right_frame, wrap=tk.WORD, width=50, height=10, font=font2, background="antique white")
response_entry.pack(pady=10)
response_entry.config(state="disabled")

root.mainloop()
