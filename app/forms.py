"""
This module contains the LoanForm class, which is a FlaskForm used for capturing loan application data.
Attributes:
    first_name (StringField): Field for capturing the first name of the applicant.
    last_name (StringField): Field for capturing the last name of the applicant.
    age (IntegerField): Field for capturing the age of the applicant.
    loan_amount (IntegerField): Field for capturing the loan amount requested by the applicant.
    annual_income (IntegerField): Field for capturing the annual income of the applicant.
    employment_length (IntegerField): Field for capturing the length of employment of the applicant.
    home_ownership (SelectField): Field for selecting the type of home ownership of the applicant.
    q1 (SelectField): Field for selecting the response to the question "How do you typically handle your monthly bills?".
    q2 (SelectField): Field for selecting the response to the question "If you unexpectedly received a large medical bill or had an emergency expense, how would you cover it?".
    q3 (SelectField): Field for selecting the response to the question "What is your approach to managing credit card debt?".
    q4 (SelectField): Field for selecting the response to the question "How do you handle new loan opportunities?".
    q5 (SelectField): Field for selecting the response to the question "How often do you review your credit report or track your credit score?".
    submit (SubmitField): Field for submitting the loan application form.
"""



from flask_wtf import FlaskForm
from wtforms import IntegerField, SelectField, SubmitField, StringField
from wtforms.validators import DataRequired, NumberRange, Length, InputRequired, ValidationError


class LoanForm(FlaskForm):
    # constraints are based on the dataset used to train the model
    first_name = StringField('First Name', validators=[DataRequired(), Length(min=2, max=20)])
    last_name = StringField('Last Name', validators=[DataRequired(), Length(min=2, max=20)])
    age = IntegerField('Age', validators=[DataRequired(), NumberRange(min=18, max=80)])
    loan_amount = IntegerField('Loan Amount (USD)', validators=[DataRequired(), NumberRange(min=500, max=25000)])
    annual_income = IntegerField('Annual Income (USD)', validators=[DataRequired(), NumberRange(min=4000, max=500000)]) 
    employment_length = IntegerField('Employment Length', validators=[DataRequired(), NumberRange(min=1, max=60)])
    home_ownership = SelectField('Home Ownership', choices=[('', 'Select an option'),('RENT', 'Rent'), ('OWN', 'Own'), ('MORTGAGE', 'Mortgage'), ('OTHER', 'Other')], validators=[DataRequired()]) # choices is a list of tuples, with the first element being the value and the second being the label, the label is what the user sees, the value is what the program sees

    def validate_employment_length(form, field): # custom validator
        if field.data > form.age.data - 16: # assuming the applicant can't work before the age of 16
            raise ValidationError('Invalid employment length.')

    q1 = SelectField('How do you typically handle your monthly bills?', choices=[('', 'Select an option'),
        (4, 'I pay all of them on time, without reminders.'),
        (3, 'I usually pay on time, but sometimes I need reminders.'),
        (2, 'I occasionally miss payments and catch up later.'),
        (1, 'I often struggle to pay them on time.')
    ], validators=[InputRequired()])

    q2 = SelectField('If you unexpectedly received a large medical bill or had an emergency expense, how would you cover it?', choices=[('', 'Select an option'),
        (4, 'I would use my savings.'),
        (3, 'I would pay with a credit card and pay it off quickly.'),
        (2, 'I would take out a loan or borrow from friends/family.'),
        (1, 'I’m not sure how I would cover it.')
    ], validators=[InputRequired()])

    q3 = SelectField('What is your approach to managing credit card debt?', choices=[('', 'Select an option'),
        (4, 'I pay off my credit card balance in full every month.'),
        (3, 'I pay more than the minimum amount but not the full balance.'),
        (2, 'I pay only the minimum amount due.'),
        (1, 'I often miss credit card payments.')
    ], validators=[InputRequired()])

    q4 = SelectField('How do you handle new loan opportunities?', choices=[('', 'Select an option'),
        (4, 'I carefully assess if I can comfortably afford the loan before applying.'),
        (3, 'I sometimes take on loans even if it’s tight financially.'),
        (2, 'I usually take on loans when I need them, without too much consideration.'),
        (1, 'I have taken loans before that were hard to repay.')
    ], validators=[InputRequired()])

    q5 = SelectField('How often do you review your credit report or track your credit score?', choices=[('', 'Select an option'),
        (4, 'I regularly check my credit report and monitor my score.'),
        (3, 'I check it once in a while, but not regularly.'),
        (2, 'I don’t check it often, but I know it’s important.'),
        (1, 'I’ve never checked my credit report or tracked my score.')
    ], validators=[InputRequired()])
   

    # 'Yes' is what the user inputs, '1' is what the program sees (form.question_1.data)
    

    submit = SubmitField('Submit')