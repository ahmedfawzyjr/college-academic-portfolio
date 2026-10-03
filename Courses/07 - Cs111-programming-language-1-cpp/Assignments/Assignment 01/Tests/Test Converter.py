import os, subprocess, sys

def test_converter():
    test_dir = os.path.dirname(os.path.abspath(__file__))
    sol_file = os.path.join(test_dir, '..', 'solution', 'converter_solution.cpp')
    exe_file = os.path.join(test_dir, 'converter.exe')
    
    res = subprocess.run(['g++', '-std=c++17', sol_file, '-o', exe_file], capture_output=True, text=True)
    assert res.returncode == 0, f'Compilation failed: {res.stderr}'

    proc = subprocess.run([exe_file], input='1\n25\n', text=True, capture_output=True)
    assert '77' in proc.stdout, f'Expected 77 in output, got: {proc.stdout}'
    print('Assignment 01 Converter Test Passed!')
    if os.path.exists(exe_file):
        os.remove(exe_file)

if __name__ == '__main__':
    test_converter()
