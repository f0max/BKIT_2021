from radish import given, when, then
import sys, os

sys.path.append(os.getcwd())
from main import *

@given("Coefs are {:g}, {:g} and {:g}")
def coefs(step, num1, num2, num3):
    step.context.num1 = num1
    step.context.num2 = num2
    step.context.num3 = num3

@when("Counting roots")
def finding_roots(step):
    step.context.result = reverse_roots(get_roots(step.context.num1, \
        step.context.num2, step.context.num3))

@then("The roots are {:g}, {:g}, {:g} and {:g}")
def result(step, root1, root2, root3, root4):
    result = [root1, root2, root3, root4]
    assert set(step.context.result) == set(result)