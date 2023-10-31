def test_digital_root():
    assert digital_root(20) == 7  #dois dígitos
    assert digital_root(850) == 6  #três dígitos
    assert digital_root(569843) == 6  #seis dígitos
    assert digital_root(789567) == 2  #seis dígitos

test_digital_root()  

from root import digital_root

