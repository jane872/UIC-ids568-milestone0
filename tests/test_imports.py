 

def test_numpy_import():
 
    import numpy
    assert numpy.__version__ == "1.24.3", f"expect numpy 1.24.3，actual{numpy.__version__}"

def test_pandas_import():
    
    import pandas
    assert pandas.__version__ == "2.0.3", f"expect pandas 2.0.3，actual{pandas.__version__}"

def test_pytest_import():
   
    import pytest
    assert pytest.__version__ == "7.4.0", f"expect pytest 7.4.0，actual{pytest.__version__}"
