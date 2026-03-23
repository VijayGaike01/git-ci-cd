def analyze_logs(file_path):
    info_count = 0
    error_count = 0

    with open(file_path, 'r') as file:
        for line in file:
            if "INFO" in line:
                info_count += 1
            elif "ERROR" in line:
                error_count += 1

    print("Log Summary:")
    print(f"INFO count: {info_count}")
    print(f"ERROR count: {error_count}")


if __name__ == "__main__":
    analyze_logs("data/sample.log")
    