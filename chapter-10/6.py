class CustomException(Exception):
    pass
def raise_custom_exception():
    try:
        raise CustomException("this is a custom exception")
    except CustomException as e:
        print(e)

raise_custom_exception()