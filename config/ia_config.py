import os
import google.generativeai as genai

genai.configure(api_key=os.environ["GEMINI_API"])

# Create the model
generation_config = {
  "temperature": 1,
  "top_p": 0.95,
  "top_k": 64,
  "max_output_tokens": 8192,
  "response_mime_type": "text/plain",
}

model = genai.GenerativeModel(
  model_name="gemini-1.5-flash",
  generation_config=generation_config,
  system_instruction="seu nome será luna\nvoce só podera falar sobre musica\nvoce sera capaz de indentificar musicas atraves das emoções\ntente compreender o usuario para achar musicas através do que ele dizer",
)

chat_session = model.start_chat(
  history=[
      
  ]
)
