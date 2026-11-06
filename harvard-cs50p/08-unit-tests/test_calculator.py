from calculator import square


def main():
    test_square()


def test_square():
    try:
        assert square(5) == 25, f"Expected 25 but got {square(5)}"
        assert square(3) == 9, f"Expected 9 but got {square(3)}"
        assert square(0) == 0, f"Expected 0 but got {square(0)}"
        assert square(-3) == 9, f"Expected 9 but got {square(-3)}"
        print("All tests passed!")
    except AssertionError as e:
        print(f"Test failed: {e}")
        raise

if __name__ == "__main__":
    main()
