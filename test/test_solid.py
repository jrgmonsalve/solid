from open_close import good

def test_ocp_good_circle():
    # Arrage
    circle: good.Shape = good.Circle(20)
    
    # Act
    area = circle.calculate_area()

    # Assert
    assert area  == 1256.6370614359173