import os

def test_srs():
    test_dir = os.path.dirname(os.path.abspath(__file__))
    srs_path = os.path.join(test_dir, '..', 'solution', 'srs_document.md')
    assert os.path.exists(srs_path), f'Missing SRS doc at {srs_path}'
    print('Software Engineering Assignment 01 Test Passed!')

if __name__ == '__main__':
    test_srs()
