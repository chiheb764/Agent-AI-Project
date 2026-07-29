from typing import TypedDict
from langgraph.graph import StateGraph, END

from cal import calculatrice
from pypdf import PdfReader
from docx import Document


class AgentState(TypedDict):
    question: str
    reponse: str
    type_question: str
def calculatrice(expression):
 return eval(expression)

def analyse_node(state):
    print("Analyse de la question...")
    return state


def reponse_node(state):
    question = state["question"]
    state["reponse"] = f"Votre question est : {question}"
    return state
def decision_node(state):
    question = state[
    "question"
    ].lower()
    if (
        "+" in question
        or "-" in question
        or "*" in question
        or "/" in question
        ):
        state["type_question"] = (
        "calcul"
        )
    elif ".pdf" in question:
        state["type_question"] = (
        "pdf"
        )
    elif ".docx" in question:

        state["type_question"] = (
        "docx"
        )
    elif ".txt" in question:
        state["type_question"] = (
        "txt"
        )
    else:
        state["type_question"] = (
        "documentation"
        )
    return state
def calculatrice_node(state):
    question = state["question"]
    resultat = calculatrice(
    question
    )
    state["reponse"] = str(
    resultat
    )
    return state
def documentation_node(state):
    state["reponse"] = (
    "Réponse documentaire"
    )
    return state
def greeting_node(state):
    state["reponse"] = (
    "Bonjour ! Comment puis-je vous aider ?"
    )
    return state
def route_question(state):
    return state[
    "type_question"
    ]
def decision_node(state):
    question = state[
    "question"
    ].lower()
    if "bonjour" in question:
        state["type_question"] = (
        "salutation"
        )
    elif (
        "+" in question
        or "-" in question
        or "*" in question
        or "/" in question
        ):
        state["type_question"] = (
        "calcul"
        )
    elif ".pdf" in question:
        state["type_question"] = (
        "pdf"
        )
    elif ".docx" in question:
        state["type_question"] = (
        "docx"
        )
    elif ".txt" in question:
        state["type_question"] = (
        "txt"
        )
    else:
        state["type_question"] = (
        "documentation"
        )
    return state
def txt_reader_node(state):
    contenu = txt_reader(
    "documents/rh.txt"
    )
    state["reponse"] = contenu
    return state
def txt_reader(chemin_fichier):
    with open(
    chemin_fichier,
    "r",
    encoding="utf-8"
    ) as fichier:
      contenu = fichier.read()
    return contenu
def pdf_reader(chemin_fichier):
    lecteur = PdfReader(
    chemin_fichier
    )
    contenu = ""
    for page in lecteur.pages:
        contenu += (
        page.extract_text()
        )
    return contenu

def docx_reader(chemin_fichier):
    doc = Document(
    chemin_fichier
    )
    contenu = ""
    for paragraphe in doc.paragraphs:
        contenu += (
        paragraphe.text + "\n"
        )
    return contenu
def pdf_reader_node(state):
    contenu = pdf_reader(
    "formation.pdf"
    )
    state["reponse"] = contenu
    return state
def docx_reader_node(state):
    contenu = docx_reader(
    "procedure.docx"
    )
    state["reponse"] = contenu
    return state
workflow = StateGraph(AgentState)


workflow.add_node("analyse", analyse_node)
workflow.add_node("reponse", reponse_node)
workflow.add_node(
"decision",
decision_node
)
workflow.add_node(
"calculatrice",
calculatrice_node
)
workflow.add_node(
"documentation",
documentation_node
)
workflow.add_node(
"salutation",
greeting_node
)
workflow.add_node(
"txt_reader",
txt_reader_node
)
workflow.add_node(
"pdf_reader",
pdf_reader_node
)
workflow.add_node(
"docx_reader",
docx_reader_node
)

workflow.add_conditional_edges(
"decision",
route_question,
{
"calcul":
"calculatrice",
"pdf":
"pdf_reader",
"docx":
"docx_reader",
"txt":
"txt_reader",
"documentation":
"documentation"
})

workflow.set_entry_point("analyse")


workflow.add_edge(
"analyse",
"decision"
)
workflow.add_edge(
"documentation",
END
)
workflow.add_edge(
"calculatrice",
END
)
workflow.add_edge(
"salutation",
END
)
workflow.add_edge("reponse", END)
workflow.add_edge(
"salutation",
END
)
workflow.add_edge(
"txt_reader",
END
)
workflow.add_edge(
"pdf_reader",
END
)
workflow.add_edge(
"docx_reader",
END
)

agent = workflow.compile()


resultat = agent.invoke(
{"question": "50+25"}
)
print(resultat)
resultat = agent.invoke(
{"question": "Lis formation.pdf"}
)
print(resultat)


#print(resultat["reponse"])
#print(txt_reader("documents/rh.txt")
#print(pdf_reader(r"C:\Users\hp\Desktop\Projet_Agent_Documentaire\formation.pdf"))
#print(docx_reader(r"C:\Users\hp\Desktop\Projet_Agent_Documentaire\procedure.docx"))


