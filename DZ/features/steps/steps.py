from behave import Given, When, Then
import os, sys

sys.path.append(os.getcwd())
from bot.messages import camp_message
from bot.answers import location, backpack, transport


@Given("answers for states 1, 2, 3 : {num1}, {num2}, {num3}")
def given_answers(context, num1, num2, num3):
    context.ans1 = int(num1)
    context.ans2 = int(num2)
    context.ans3 = int(num3)

@When("setting camp")
def setting_camp(context):
    res = camp_message.format(loc=location.get(context.ans1), bp=backpack.get(context.ans2), transp=transport.get(context.ans3))
    context.result = res

@Then("we should see В итоге: Локация: {loc}. В рюкзаке: {bp}. Способ передвижения: {transp}. /setstate, чтобы очистить и собрать заново.")
def check_result(context, loc, bp, transp):
    res = 'В итоге:\nЛокация: ' + str(loc) + '.\nВ рюкзаке: ' + str(bp) + '.\nСпособ передвижения: ' + str(transp) + '.\n/setstate, чтобы очистить и собрать заново.'
    assert(context.result == res)