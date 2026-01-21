 

def test_numpy_import():
 
    import numpy
    assert numpy.__version__ == "1.26.3", f"expect numpy 1.26.3，actual{numpy.__version__}"

def test_pandas_import():
    
    import pandas
    assert pandas.__version__ == "2.1.4", f"expect pandas 2.1.4，actual{pandas.__version__}"

def test_pytest_import():
   
    import pytest
    assert pytest.__version__ == "9.0.2", f"expect pytest 9.0.2，actual{pytest.__version__}"
