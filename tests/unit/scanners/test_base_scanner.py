import os
import sys
import pytest
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "..", "src"))
from scanners.base_scanner import BaseScanner

# Create a simple subclass of BaseScanner for testing purposes before running the tests. 
class _TestScanner(BaseScanner):
    def _scan(self, content: str):
        return content
    
@pytest.fixture(scope="module")
def scanner():
    """Create one scanner instance for all tests in this module."""
    return _TestScanner()


def test_open_file_success(tmp_path, scanner):
    """Test that the BaseScanner can open a file successfully."""
    content = "This is a test."
    test_file = tmp_path / "test.txt" 
    test_file.write_text(content)

    result = scanner.scan(str(test_file))
    assert result == content

def test_open_file_not_found(scanner):
    """Test that the BaseScanner raises a FileNotFoundError when the file does not exist."""
    with pytest.raises(FileNotFoundError):
        scanner.scan("non_existent_file.txt")
    assert True

def test_abstract_method_enforcement():
    """Test that the BaseScanner cannot be instantiated directly."""
    with pytest.raises(TypeError):
        BaseScanner()
    assert True

