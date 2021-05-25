from copy import deepcopy

questions_template = {
    'title': 'default title',
    'question': 'default question',
    'answer': 'default answer',
    'hints': []
}

def make_new_question(title, question, answer, hints=None):
    new_q = deepcopy(questions_template)

    # required fields
    new_q['title'] = title
    new_q['question'] = question
    new_q['answer'] = answer

    # optional fields
    if hints is not None:
        new_q['hints'] = hints

    return new_q


question_1 = make_new_question("title1", "question1", "answer1",
                                ["q1 hint1", "q1 hint2"])
question_2 = make_new_question("title2", "question2", "answer2")
question_3 = make_new_question("title3", "question3", "answer3",
                                ["q3 hint1"])

print(question_1)
print(question_2)
print(question_3)
