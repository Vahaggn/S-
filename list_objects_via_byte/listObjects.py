import subprocess

bucket_name = "EXAMPLE" #Write your Bucket name
base_path = "FOLDER1/FOLDER2" #Write your object path

#if in following path you have different folders you can use following for loop if not just skip it

for pattern_number in range(1, 10):
    pattern = f"{pattern_number}"  # Creates pattern like PATTERN001, PATTERN002, ...
    s3cmd_command = f"s3cmd --config=/app/s3cfg ls s3://{bucket_name}/{base_path}/{pattern}/ | awk '$3 < 1'"

    try:
        file_path = "output.txt"  
        with open(file_path, "a") as file:
            text_to_append = f"Path Number {pattern}\n"  
            file.write(text_to_append)
            print(f"Path Number {pattern}")
        output = subprocess.check_output(s3cmd_command, shell=True, stderr=subprocess.STDOUT, text=True)
        with open(file_path, "a") as output_file:
            output_file.write(output)

    except subprocess.CalledProcessError as e:
        print(f"Path Number {pattern} does not exist.")