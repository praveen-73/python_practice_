def main_process():
    print("Starting process")

    data = get_data()
    validated_data = validate_data(data)
    save_data(validated_data)

    print("Process completed")


def get_data():
    print("Getting data...")
    return "Patient Data"


def validate_data(data):
    print("Validating:", data)
    return "Validated Patient Data"


def save_data(data):
    print("Saving:", data)


main_process()