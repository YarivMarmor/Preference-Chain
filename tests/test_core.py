import sys
from pathlib import Path
sys.path.insert(0,str(Path(__file__).resolve().parents[1]/'src'))
from preference_core import preference_distance
import pytest

def test_workbook_cal():
    r=preference_distance([1,1,5,1,2,3,4],[1,2,2,2,3,4,5])
    assert r['numerator']==20 and r['norm1']==36 and r['norm2']==36
    assert r['cosine']==pytest.approx(0.5555555555555556)
    assert r['distance']==pytest.approx(0.31250561891173007)
def test_reverse():
    assert preference_distance([1,2,3],[3,2,1])['distance']==pytest.approx(1)
def test_identical():
    assert preference_distance([1,2,2],[1,2,2])['distance']==pytest.approx(0)
def test_all_tied():
    with pytest.raises(ValueError): preference_distance([1,1,1],[1,2,3])
def test_wrong_length():
    with pytest.raises(ValueError): preference_distance([1,2,3],[1,2])
def test_noninteger():
    with pytest.raises(ValueError): preference_distance([1.5,2,3],[1,2,3])
