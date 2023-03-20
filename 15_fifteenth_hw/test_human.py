"""
Test the Human class in the attached file. I will check the coverage. Write as much TCs as possible
"""
import pytest


@pytest.mark.smoke
def test_change_gender_to_male(create_female_age_30):
    human = create_female_age_30
    new_gender = 'male'
    human.change_gender(new_gender)
    assert human.gender == new_gender, f'Gender was not changed to {new_gender}'


@pytest.mark.smoke
def test_change_gender_to_female(create_male_age_40):
    human = create_male_age_40
    new_gender = 'female'
    human.change_gender(new_gender)
    assert human.gender == new_gender, f'Gender was not changed to {new_gender}'


@pytest.mark.regression
def test_not_change_incorrect_gender(create_female_age_30):
    human = create_female_age_30
    new_gender = 'ololo'
    with pytest.raises(Exception):
        human.change_gender(new_gender)
    assert human.gender != new_gender, f'Gender was changed to {new_gender}'


@pytest.mark.regression
def test_not_change_the_same_gender(create_female_age_30):
    human = create_female_age_30
    the_same_gender = 'female'
    with pytest.raises(Exception):
        human.change_gender(the_same_gender)
    assert human.gender == the_same_gender, f'Gender was changed to {the_same_gender}'


# there's a bug in the code logic "__is_alive"
@pytest.mark.regression
@pytest.mark.xfail
def test_not_change_gender_of_dead_human(create_human_with_params):
    human = create_human_with_params(name='Mia', age=100, gender='female')
    new_gender = 'male'
    human.change_gender(new_gender)
    assert human.gender == new_gender, f'Gender was changed to dead human'


@pytest.mark.smoke
def test_change_age(create_human_with_params):
    age = 30
    human = create_human_with_params('Mia', age, 'female')
    human.grow()
    assert human.age == age + 1, 'Age was not changed'


@pytest.mark.regression
def test_dead_age(create_human_with_params):
    age = 100
    human = create_human_with_params('Mia', age, 'female')
    human.grow()
    assert human.age != age + 1, 'Human is already dead'


# there's a bug in the code logic "grow"
@pytest.mark.regression
@pytest.mark.xfail
def test_not_born_human(create_human_with_params):
    age = -2
    human = create_human_with_params('Mia', age, 'female')
    human.grow()
    assert human.age == age + 1, 'Human was not born yet'
