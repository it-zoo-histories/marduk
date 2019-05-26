## story_hello
* dialog_greet
  - utter_greet

## story_goodbye
* dialog_bye
  - utter_goodbye
  
## story_expect_prognoz_weather
* expect_prognoz_weather
  - utter_test_weather

## story_expect_city_action
* expect_city_action{"cityAction": "прогноз погоды"}
  - utter_test_weather

## story_probki
* dialog_greet
  - utter_greet
* expect_city_action
  - utter_action_on_it
* dialog_question_affirm
  - utter_questionNow
* dialog_question_affirm OR dialog_question_deny
  - utter_thanks_to_user
* dialog_thanks OR dialog_bye
  - utter_review
