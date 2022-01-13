from unittest import TestLoader, TestSuite
from pyunitreport import HTMLTestRunner
from assertions import AssertionTest
from searchtests import HomeTest

assertions_test = TestLoader().loadTestsFromTestCase(AssertionTest)
search_test = TestLoader().loadTestsFromTestCase(HomeTest)

smoke_test = TestSuite([assertions_test, search_test])

kwargs = {
    "output": 'smoke-report'
}

runner = HTMLTestRunner(**kwargs)
runner.run(smoke_test)