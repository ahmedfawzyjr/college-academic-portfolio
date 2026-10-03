import os, subprocess

def test_lcs():
    test_dir = os.path.dirname(os.path.abspath(__file__))
    sol_file = os.path.join(test_dir, '..', 'solution', 'lcs_solution.cpp')
    exe_file = os.path.join(test_dir, 'lcs_test.exe')
    
    res = subprocess.run(['g++', '-std=c++17', sol_file, '-o', exe_file], capture_output=True, text=True)
    assert res.returncode == 0, f'Compilation failed: {res.stderr}'
    proc = subprocess.run([exe_file], capture_output=True, text=True)
    assert '4' in proc.stdout, f'Output: {proc.stdout}'
    print('Algorithms Assignment 01 LCS Test Passed!')
    if os.path.exists(exe_file):
        os.remove(exe_file)

if __name__ == '__main__':
    test_lcs()
