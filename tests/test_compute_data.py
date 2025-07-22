from unittest.mock import Mock
from pathlib import Path
from inflammation.compute_data import CSVDataSource
import numpy.testing as npt

def test_analyse_data_mock_source():
    from inflammation.compute_data import analyse_data
    data_source = Mock()
  
    # TODO: configure data_source mock
    data_source.load_inflammation_data.return_value = [
        [[0, 1, 2], [3, 4, 5]],
        [[1, 2, 3], [4, 5, 6]]
    ]

    mock_data = [
        [0, 1, 2], 
        [3, 4, 5],
        [1, 2, 3],
        [4, 5, 6]
    ]
    #data_source.load_inflammation_data.return_value = mock_dat
    analyse_data(data_source)


def test_analyse_data():
    from inflammation.compute_data import analyse_data
    path = Path.cwd() / "data"
    data_source = CSVDataSource(path)
    result = analyse_data(data_source)
    #print(result)
    
    # TODO: add assert statement(s) to test the result value is as expected
    test_input = [0.        , 0.22510286, 0.18157299, 0.1264423 , 0.9495481 ,
       0.27118211, 0.25104719, 0.22330897, 0.89680503, 0.21573875,
       1.24235548, 0.63042094, 1.57511696, 2.18850242, 0.3729574 ,
       0.69395538, 2.52365162, 0.3179312 , 1.22850657, 1.63149639,
       2.45861227, 1.55556052, 2.8214853 , 0.92117578, 0.76176979,
       2.18346188, 0.55368435, 1.78441632, 0.26549221, 1.43938417,
       0.78959769, 0.64913879, 1.16078544, 0.42417995, 0.36019114,
       0.80801707, 0.50323031, 0.47574665, 0.45197398, 0.22070227]
    npt.assert_array_almost_equal(result, test_input, )


def test_compute_standard_deviation_by_data():
    from inflammation.compute_data import compute_standard_deviation_by_day
    # Test input data two days
    test_input = [
        [[0, 1, 2], [3, 4, 5]],
        [[1, 2, 3], [4, 5, 6]]
    ]
    
    # Expected output data
    expected_output = [0.5, 0.5, 0.5]
    
    # Call the function with the test input
    result = compute_standard_deviation_by_day(test_input)
    
    # Assert that the result matches the expected output
    npt.assert_array_almost_equal(result, expected_output)

    test_input = [
        [[0, 1, 2]], [[3, 4, 5]]
    ]
    expected_output = [1.5, 1.5, 1.5]
    result = compute_standard_deviation_by_day(test_input)
    npt.assert_array_almost_equal(result, expected_output)

    test_input = [[[0, 1, 2]]]
    expected_output = [0, 0, 0]
    result = compute_standard_deviation_by_day(test_input)
    npt.assert_array_almost_equal(result, expected_output)

    test_input = [[[]]]
    expected_output = [[[]]]
    result = compute_standard_deviation_by_day(test_input)
    npt.assert_array_almost_equal(result, expected_output)


