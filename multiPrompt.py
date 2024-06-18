import re

def read_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        return file.read()

def parse_questions(text):
    pattern = re.compile(r'(\d+)\. (.+)')
    matches = pattern.findall(text)
    
    questions = []
    for match in matches:
        question_number = int(match[0])
        question_text = match[1].strip()
        
        questions.append({
            'number': question_number,
            'question': question_text
        })
    
    return questions

file_path = 'promptDatos.txt'
text = read_file(file_path)
questions = parse_questions(text)

for question in questions:
    print(f"Pregunta {question['number']}: {question['question']}")

# Print the full list of questions
print("\nLista completa de preguntas:")
for question in questions:
    print(question)
    print("----------")
