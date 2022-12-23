import openai
import os
import streamlit as st

openai.api_key = os.getenv("OPENAI_API_KEY")

st.header("Evaluador de ensayos")

# Inicializa el modelo de lenguaje GPT-3
model_engine = "text-davinci-003"

# Crea una caja de diálogo para que el usuario ingrese su solicitud
essay = st.text_area("Pegue su ensayo:")

# Genera una respuesta utilizando el modelo de lenguaje GPT-3
if essay:
    prompt = (f"Su tarea es evaluar la calidad de los ensayos académicos que se le presentan." 
              f"Evalúelos como lo haría un profesor de Harvard y póngales una nota de cero a cien." 
              f"Dé tres evaluaciones, como si fueran tres evaluadores." 
              f"El ensayo debe tener al menos cinco párrafos; de lo contrario diga 'Extensión insuficiente. Se requieren al menos cinco párrafos.' y no lo evalúe.\n{essay}\n")
    completions = openai.Completion.create(
        engine=model_engine,
        prompt=prompt,
        max_tokens=1024,
        temperature=0.5,
        top_p=1,
        frequency_penalty=0.5,
        presence_penalty=0.5
    )

    message = completions.choices[0].text

    # Obtiene la respuesta generada y la muestra en otra caja de diálogo
    response = completions.choices[0].text
    st.markdown(f"**Respuesta:** {response}")
