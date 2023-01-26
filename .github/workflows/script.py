name: CI
'on':
- push
- pull_request
- workflow_dispatch
jobs:
  test-cpp:
    runs-on: ubuntu-latest
    env:
      OLC_PATH: cpp
    steps:
    - uses: actions/checkout@v2
    - name: test
      run: bazel test --test_output=all ${OLC_PATH}:all
    - name: check formatting
      run: cd ${OLC_PATH} && bash clang_check.sh
