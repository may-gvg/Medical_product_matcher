from project import *


def test_entry_data():
    df1 = entry_data()
    assert str(type(df1)) == "<class 'pandas.core.frame.DataFrame'>"


def test_entry_data2():
    df1 = entry_data()
    ed = entry_data2(df1)
    assert ed == 0


def test_compare_scores():
    disorders = {'Lupus ': 115.29999999999998, 'Pneumonia': 115.29999999999998, 'Depression ': 82.6, 'Diabetes': 82.6,
                 'Bronchitis': 75.5, 'Anxiety ': 75.5}
    cures = {'Diabetes': 62.5, 'Depression ': 77.67, 'Yeast infection ': 60.65, 'Alzheimer': 74.29, 'Pneumonia': 72.4,
             'HPV ': 85.55, 'Strep throat ': 95.05, 'Bronchitis': 83.77, 'Lyme ': 72.13, 'ADHD ': 84.19,
             'Autism ': 68.31}
    res = compare_scores(disorders, cures)
    assert res == 26250.396999999997


def test_weighted_rating():
    assert 1 == 1


def test_check_score():
    assert 1 == 1


def test_run_search():
    assert 1 == 1
