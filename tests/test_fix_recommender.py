# test_fix_recommender.py
# Unit tests for fix_recommender module

import pytest
from fix_recommender import recommend_fix

def test_crash_loop():
    diagnosis = "Pod entered CrashLoopBackOff state due to an application crash."
    result = recommend_fix(diagnosis)
    assert any("restart" in fix.lower() for fix in result)

def test_missing_env_var():
    diagnosis = "The application failed to start due to missing environment variable DB_PASSWORD."
    result = recommend_fix(diagnosis)
    assert any("configmap" in fix.lower() or "secret" in fix.lower() for fix in result)

def test_image_pull_error():
    diagnosis = "ImagePullBackOff due to invalid image tag."
    result = recommend_fix(diagnosis)
    assert any("image" in fix.lower() for fix in result)

def test_no_diagnosis():
    diagnosis = "All systems appear operational."
    result = recommend_fix(diagnosis)
    assert result == ["No obvious fix suggested. Please review the diagnosis manually."]
