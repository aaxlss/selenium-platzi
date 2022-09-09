from unittest import TestLoader, TestSuite
from pyunitreport import HTMLTestRunner
from SearchTest import SearchTest
from AssertionTest import AssertionTest

assertion_test = TestLoader().loadTestsFromTestCase(AssertionTest)
search_test = TestLoader().loadTestsFromTestCase(SearchTest)

smoke_test = TestSuite([assertion_test, search_test])

kwargs = {
    'output': 'smoke_report',
    'report_name': 'SmokeReport'
}

runner = HTMLTestRunner(**kwargs)
runner.run(smoke_test)