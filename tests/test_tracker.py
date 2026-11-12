# tests/test_tracker.py
import pytest
from tracker import Tracker

def test_add_application(tmp_path):
    # Use a temp file specifically for testing
    test_file = tmp_path / "test_data.json"
    tracker = Tracker(data_file=test_file)
        
    tracker.add("Test Org", "Contact Name", "test@test.com", "Engineering", "Test City", "Sample note")
    assert len(tracker.apps) == 1
    assert tracker.apps[0].org == "Test Org"
    assert test_file.exists()

def test_load_applications(tmp_path):
    test_file = tmp_path / "test_data.json"
    tracker = Tracker(data_file=test_file)
    tracker.add("Org 1", "Contact 1", "org1@test.com", "Admin", "City 1")
        
    # Re-instantiate to test loading from file
    new_tracker = Tracker(data_file=test_file)
    assert len(new_tracker.apps) == 1
    assert new_tracker.apps[0].org == "Org 1"