import random

def generate_tests(num_students):
    # Wczytywanie krajów i stolic z pliku
    with open("stolice.txt", 'r', encoding='utf-8') as f:
        lines = f.readlines()
    questions = []
    answers = {}
    for line in lines:
        question, answer = line.strip().split(';')
        questions.append(question)
        answers[question] = answer

    # Pomieszaj pytania i utwórz listę pytań dla wszystkich studentów
    # random.shuffle(questions)
    # question_sets = [questions for i in range(num_students)]
    question_sets = []
    for i in range(num_students):
        questions_copy = questions.copy()
        random.shuffle(questions_copy)
        question_sets.append(questions_copy)

    # Wygeneruj plik z testem i kluczem odpowiedzi dla każdego studenta
    for i, question_set in enumerate(question_sets):
        with open(f'spr{i+1}.txt', 'w', encoding='utf-8') as test_file, open(f'odp{i+1}.txt', 'w', encoding='utf-8') as ans_file:
            test_file.write("Imię i nazwisko:\n\n")
            test_file.write("Data:\n\n")
            test_file.write("Semestr:\n\n")
            test_file.write(f"\t\tStolice - sprawdzian (Formularz {i + 1})\n\n")
            for question in question_set:
                # Wygeneruj listę 4 odpowiedzi, w której jedna jest prawidłowa oraz zapobiegnij powtórzeniom
                # all_answers = [answers[question]] + [random.choice(list(answers.values())) for _ in range(3)]
                all_answers = [answers[question]]
                remaining_answers = list(answers.values())
                remaining_answers.remove(answers[question])
                for l in range(3):
                    answer = random.choice(remaining_answers)
                    all_answers.append(answer)
                    remaining_answers.remove(answer)

                random.shuffle(all_answers)
                test_file.write(f"{question_set.index(question)+1}. Jaką stolicę ma państwo {question}?\n")
                for j, ans in enumerate(all_answers):
                    test_file.write(f"\t{chr(j + ord('A'))}. {ans}\n")
                test_file.write("\n")
                ans_file.write(f"{question_set.index(question)+1}. {chr(all_answers.index(answers[question])+ ord('A'))}\n")


students = int(input("Dla ilu studentów chcesz wygenerować testy? "))
generate_tests(students)