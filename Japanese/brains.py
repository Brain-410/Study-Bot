import random, os, time
import knowledge
os.system('cls')
learning = knowledge.kanji

questions, answers, score, total = list(learning.keys()), list(learning.values()), 0, 0
while True:
    x = random.randint(0, len(learning)-1)
    print(f'{total+1}: {questions[x]}')
    human_answer = input('>>> ').lower()
    if human_answer == 'break':
        try:
            print(f'{round(score/total)}% accuracy')
        except ZeroDivisionError:
            print('0%')
        break
    if human_answer != answers[x].lower():
        print(f'Incorrect:\n{answers[x]}')
        input()
    else:
        print('Correct\n')
        score += 100
        time.sleep(0.2)
    total += 1
    os.system('cls') 
 