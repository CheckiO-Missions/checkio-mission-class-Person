init_code = """
if not "Person" in USER_GLOBAL:
    raise NotImplementedError("Where is 'Person'?")

Person = USER_GLOBAL['Person']
"""

run_test = """
RET['code_result'] = {}
"""


def prepare_test(test="", answer=None, middle_code="\n", show_code=None):
    if show_code is None:
        show_code = middle_code + test
    if not test:
        return_code = "\nRET['code_result'] = ''"
        answer = ''
    else:
        return_code = run_test.format(test)
    return {"test_code": {"python-3": init_code + middle_code + return_code},
            "show": {"python-3": show_code},
            "answer": answer}


TESTS = {
    "1. Name": [
        prepare_test(test="Person('John', 'Smith', '19.09.1979', 'welder', 15, 3600, 'Canada', 'Vancouver', 'male').name()",
                     answer="John Smith"),
        prepare_test(test="Person('Adam', 'Greene', '24.12.1961', 'director', 36, 11000, 'England', 'London', 'male').name()",
                     answer="Adam Greene"),
        prepare_test(test="Person('Kate', 'Hound', '05.02.2000', 'student', 0, 0, 'Australia', 'Sydney', 'female').name()",
                     answer="Kate Hound"),	
    ],
    "2. Age": [
        prepare_test(test="Person('John', 'Smith', '19.09.1979', 'welder', 15, 3600, 'Canada', 'Vancouver', 'male').age()",
                     answer=38),
        prepare_test(test="Person('Adam', 'Greene', '24.12.1961', 'director', 36, 11000, 'England', 'London', 'male').age()",
                     answer=56),
        prepare_test(test="Person('Kate', 'Hound', '05.02.2000', 'student', 0, 0, 'Australia', 'Sydney', 'female').age()",
                     answer=17)
    ],
    "3. Work, money": [
        prepare_test(test="Person('Hanna Rose', 'May', '05.12.1995', 'designer', 2.2, 2150, 'Austria', 'Vienna').work()",
                     answer='Is a designer'),
        prepare_test(test="Person('John', 'Smith', '19.09.1979', 'welder', 15, 3600, 'Canada', 'Vancouver', 'male').money()",
                     answer='648 000'),
        prepare_test(test="Person('Kate', 'Hound', '05.02.2000', 'student', 0, 0, 'Australia', 'Sydney', 'female').work()",
                     answer='She is a student'),
        prepare_test(test="Person('Adam', 'Greene', '24.12.1961', 'director', 36, 11000, 'England', 'London', 'male').money()",
                     answer='4 752 000')
    ],
    "4. Home": [
        prepare_test(test="Person('Hanna Rose', 'May', '05.12.1995', 'designer', 2.2, 2150, 'Austria', 'Vienna').home()",
                     answer='Lives in Vienna, Austria'),
        prepare_test(test="Person('John', 'Smith', '19.09.1979', 'welder', 15, 3600, 'Canada', 'Vancouver', 'male').home()",
                     answer='Lives in Vancouver, Canada'),
        prepare_test(test="Person('Kate', 'Hound', '05.02.2000', 'student', 0, 0, 'Australia', 'Sydney', 'female').home()",
                     answer='Lives in Sydney, Australia')
    ]

}
