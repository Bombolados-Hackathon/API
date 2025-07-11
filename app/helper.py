import random


def calculate_xp(user_acuracy: float) -> int:
    if user_acuracy == 100:
        return 15
    elif user_acuracy >= 80:
        return 20
    elif user_acuracy >= 60:
        return 25
    elif user_acuracy >= 40:
        return 30
    elif user_acuracy >= 20:
        return 35
    else:
        return 40


def get_random_question_type():
    question_types = ['multiple_choice', 'true_false', 'matching']
    return random.choice(question_types)
