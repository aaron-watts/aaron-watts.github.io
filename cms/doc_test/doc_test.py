"""Run tests on HTML documents"""

from doc_test.tests import tests

def test_documents(documents):
    """
    Run tests HTML documents and return boolean
    """
    passed = True
    for document in documents:
        for test in tests:
            result = test(document)
            if not result["passed"]:
                print(f"FAILED: {document['path']}\n{result['desc']}")
                passed = False
    return passed
