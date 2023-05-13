from selene import browser, have
import os

def test_registration_form():
    browser.open('/automation-practice-form')
    browser.element('#firstName').type('Nikolai')
    browser.element('#lastName').type('Danilov')
    browser.element('#userEmail').type('Danilov@gmail.com')
    browser.element('[for=gender-radio-1]').click()
    browser.element('#userNumber').type('9270535555')

    browser.element('#dateOfBirthInput').click()
    browser.element('.react-datepicker__month-select').click()
    browser.all('.react-datepicker__month-select option').should(have.size_greater_than(0)).filtered_by(have.exact_text('June')).first.click()
    browser.element('.react-datepicker__year-select').click()
    browser.all('.react-datepicker__year-select option').should(have.size_greater_than(0)).filtered_by(have.exact_text('1991')).first.click()
    browser.element('.react-datepicker__day--025').should(have.no.css_class('.react-datepicker__day--outside-month')).click()

    browser.element('#subjectsInput').type('Chemistry').press_enter()
    browser.element('#subjectsInput').type('Arts').press_enter()

    browser.element('[for="hobbies-checkbox-3"]').click()

    browser.element('#uploadPicture').set_value(os.path.join(os.path.abspath('test_photo.jpg')))

    browser.element('#currentAddress').type('Saratov')
    browser.element('#state').click()
    browser.element('#react-select-3-option-0').should(have.exact_text('NCR')).click()
    browser.element('#city').click()
    browser.element('#react-select-4-option-0').should(have.exact_text('Delhi')).click()
    browser.element('#submit').click()

    browser.element('.modal-title').should(have.exact_text('Thanks for submitting the form'))
    browser.all('tbody tr').should(have.exact_texts(
        'Student Name Nikolai Danilov',
        'Student Email Danilov@gmail.com',
        'Gender Male',
        'Mobile 9270535555',
        'Date of Birth 25 June,1991',
        'Subjects Chemistry, Arts',
        'Hobbies Music',
        'Picture test_photo.jpg',
        'Address Saratov',
        'State and City NCR Delhi'
    ))