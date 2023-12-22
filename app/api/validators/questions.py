from app.models import Form, Question


def validate_user_answer(answer_data):
    form = Form.query.filter(Form.id == answer_data["form_id"]).first()
    question = Question.query.filter(Question.id == answer_data["question_id"]).first()

    if not form:
        return "Requested form doesn't exist", 404

    if not question:
        return "Requested question doesn't exist", 404

    for question in form.questions:
        if question.id == answer_data["question_id"]:
            return ""

    return "Bad request, form and questions do not match", 400