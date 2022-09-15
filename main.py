# This is a sample Python script.

# Press Maj+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import nltk
from pdfminer.high_level import extract_text
import re

nltk.download('punkt')
nltk.download('averaged_perceptron_tagger')
nltk.download('maxent_ne_chunker')
nltk.download('words')
nltk.download('stopwords')
from flask import *
from flask_cors import CORS, cross_origin   

TECHNICAL_SKILLS_DB = [
    'machine learning',
    'data science',
    'python',
    'word',
    'excel',
    'English',
    'angular',
    'javascript',
    'java',
    'react',
    'reactJS',
    'SQL',
    'plSQL',
    'Nestjs',
    'nodeJs',
    'docker',
    'JEE',
    'react native',
    'ionic',
    'flutter',
    'android',
    'ios',
    'IOT',
    'Kotlin',
    'Spring',
    'Spring boot',
    'SpringBoot',
    'Spring-Boot',
    'c#',
    'c',
    'c++',
    'HTML',
    'CSS',
    '.Net',
    '.Net core'
    '.NetCore'
    '.Net Framework'
    '.NetFramework'
    'Php',
    'symfony',
    'laravel',
    'Odoo',
    'aws',
    'cloud',
    'azure'
    'Microsoft azure'
    'cloud computing'
    'flask',
    'Machine Learning',
    'computer vision',
    'vault',
    'Typescript',
    'firebase',
    'git'
]
EDUCATION_DB = [
    'education ',
    'formation ',
    'diplôme ',
    'diplôme national ',
    'national ',
    'institut supérieur ',
    'institut superieur ',
    'baccalaureat ',
    'baccalauréat ',
    'faculté ',
    'eleve ',
    'élève ',
    'ecole '
    'école '
    'école superieur ',
    'licence fondamentale ',
    'licence appliquée ',
    'mastere ',
    'mastere degree ',
    'mastère ',
    'mastère de recherche ',
    'mastère professionnelle ',
    'cycle d''ingenieur ',
    'Basic education ',
    'Formal education ',
    'Informal education ',
    'Self-directed learning ',
    'Private school ',
    'lycée ',
    'Public school ',
    'Primary school ',
    'Secondary school ',
    'High school ',
    'student ',
    'Study ',
    'PLAN DE FORMATION ',
    'bachelor ',
    'bachelor degree ',
    'university ',
    'university degree ',
    'engineer ',
    'engineering student ',
    'engineering degree ',
    'software engineer ',
    'faculty ',
    'school ',
    'diploma ',


]
EDUCATION_LEVELS = [
    "Certificate",
    "Bachelor",
    "PHD",
    "Doctorate",
    "master"
    "engineer",
    "ingenieur",
    "licence",
    "baccalauréat"
]
EXPERIENCE_DB = [
    'EXPÉRIENCE PROFESSIONNELLE',
    'EXPÉRIENCE',
    'work experience'
    'professional experience',
    'experience',
    'professional',
    'STAGE DE PERFECTIONNEMENT',
    'stage',
    'stage d''initiation',
    "stage de fin d'etude",
    'pfe',
    "Conception et réalisation d'un",
    "Réalisation d'un",
    'pfa',
    'PROJET DE FIN D''ANNÉE',
    'développeur fullStack',
    'développeur full Stack',
    'fullStack developer',
    'full Stack developer',
    'développeur frontend',
    'développeur front end',
    'développeur front-end',
    'frontend developer',
    'front end developer',
    'développeur backend',
    'développeur back end',
    'développeur back-end',
    'backend developer',
    'back end developer',
    'developpement'
    'dèveloppement'
    'development'
    'developer',
    'freelance',
    'stage pfe',
    'Data Scientist',
    'Data analyst',
    'stage d''été',
    'summer internship',
    'internship',
    'alternance',
    'internation',
    'end of study internship',
    'solution',
    'devops',
    'web designer',
    'designeur web',
    'CEO',
    'teacher',
    'UI-UX',
    'UI/UX',
    'UI UX',
    'integration',
    'RH',
    'Human resources',
    'Senior',
    'junior',
    "Conception et développement d",
    "développement d",
]

import json, time

app = Flask(__name__)
CORS(app)


@app.route('/', methods=['GET'])
def test():
    return "hello from flask"


@app.route('/analyseCV', methods=['POST'])
def analyse():
    cvPath = "./cvs/"+request.json['path']

    txt = extract_text_from_pdf(cvPath)
    phoneNumber = extract_phone_number(txt)
    email = extract_emails(txt)
    linkedIn = extract_linkedIn(txt)
    skills = extract_skills(txt)
    education = extract_education(txt)
    experience = extract_experience(txt)

    response = {
        "phoneNumber": phoneNumber,
        "email": email,
        "linkedIn": linkedIn,
        "skills": skills,
        "education": education,
        "experience": experience
    }
    print(response)
    return jsonify(response)


# ------------------------------------ methods --------------------------------------------

#  ----------------------------------EXTRACT TEXT FROM PDF

def extract_text_from_pdf(pdf_path):
    return extract_text(pdf_path)


# ---------------------------------------------------------ExTRACT PHONE NUMBER, EMAIL, LinkedIN


PHONE_REG = re.compile(r'[\+\(]?[1-9][0-9 .\-\(\)]{8,}[0-9]')
EMAIL_REG = re.compile(r'[a-z0-9\.\-+_]+@[a-z0-9\.\-+_]+\.[a-z]+')
LINKED_IN_PROFILE_REG = re.compile(r'^(http(s)?:\/\/)?([\w]+\.)?linkedin\.com\/(pub|in|profile)\/[a-zA-Z]+')


def extract_phone_number(resume_text):
    phone = re.findall(PHONE_REG, resume_text)
    if phone:
        for i in phone:
            if len(str(i)) == 8 or len(str(i)) == 10 or str(i).startswith('+'):
                return i

        return phone
    return None;


def extract_emails(resume_text):
    return re.findall(EMAIL_REG, resume_text)


def extract_linkedIn(resume_text):
    return re.findall(LINKED_IN_PROFILE_REG, resume_text)


def toUpperCase(item):
    return item.upper()


#---------------------------------------------------------- EXTRACT SKILLS


def extract_skills(input_text):
    stop_words = set(nltk.corpus.stopwords.words('english'))
    word_tokens = nltk.tokenize.word_tokenize(input_text)
    technical_Skills_DB = map(toUpperCase, TECHNICAL_SKILLS_DB)
    technical_Skills_DB_List = list(technical_Skills_DB)
    print("skills")
    print(technical_Skills_DB_List)
    # print(list(technical_Skills_DB))
    # remove the stop words
    filtered_tokens = [w for w in word_tokens if w not in stop_words]

    # remove the punctuation
    filtered_tokens = [w for w in word_tokens if w.isalpha()]

    # generate bigrams and trigrams (such as artificial intelligence)
    bigrams_trigrams = list(map(' '.join, nltk.everygrams(filtered_tokens, 2, 3)))

    # we create a set to keep the results in.
    found_skills = set()

    # we search for each token in our skills database
    for token in filtered_tokens:
        if token.lower() in technical_Skills_DB_List or token.upper() in technical_Skills_DB_List:
            found_skills.add(token)

    # we search for each bigram and trigram in our skills database
    for ngram in bigrams_trigrams:
        if ngram.upper() in technical_Skills_DB_List or ngram.lower() in technical_Skills_DB_List:
            found_skills.add(ngram)

    return list(found_skills)


# -----------------------------------------EXTRACT EDUCATION

def extract_education(input_text):

    education_DB_LIST = list(map(toUpperCase, EDUCATION_DB))
    found_educations = set()
    paragraphs = input_text.split('\n\n')

    for para in paragraphs:
        for item in education_DB_LIST:
            if para.upper().find(item) != -1:
                found_educations.add(para)


    return list(found_educations)


# ------------------------------------------EXTRACT EXPERIENCE

def extract_experience(input_text):

    EXPERIENCE_DB_LIST = list(map(toUpperCase, EXPERIENCE_DB))
    found_experience = set()
    paragraphs = input_text.split('\n\n')

    for para in paragraphs:
        for item in EXPERIENCE_DB_LIST:
            if para.upper().find(item) != -1:
                found_experience.add(para)

    return list(found_experience)
# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    app.run(port=7777)
