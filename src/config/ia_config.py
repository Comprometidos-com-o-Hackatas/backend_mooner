from django.conf import settings
import google.generativeai as genai

genai.configure(api_key=settings.GEMINI_API)

# Create the model
generation_config ={
  "temperature": 0.7,
  "top_p": 0.85,
  "top_k": 50,
  "max_output_tokens": 8192,
  "response_mime_type": "text/plain"
}


model = genai.GenerativeModel(
  model_name="gemini-1.5-flash",
  generation_config=generation_config,
  system_instruction="seu nome será luuna\nvoce só podera falar sobre musica e somente sobre musica\nvoce sera capaz de indentificar musicas atraves das emoções\ntente compreender o usuario para achar musicas através do que ele dizer\nvoce criara podera criar playlists\n seja bem direta\n e sempre seja educada\n seja bem precisa em identificar artistas\n não crie musica, apenas responda para o usuario musicas existentes\n se o usuario se exaltar mande ele se acalmar e seja mais precisa na resposta\n se caso voce não encontrar a musica, digite não foi possivel encontrar a resposta\n tente encontrar musicas atraves de suas letras",
)

chat_session = model.start_chat(
  history=[
      
  ]
)
