import pandas as pd

def copy_person_messages_to_text(csv_file, specific_person, output_text_file):
    # Read the CSV file
    df = pd.read_csv(csv_file)

    # Filter data for the specific person
    filtered_data = df[df['user'] == specific_person]['message']

    # Write filtered data to the specified text file
    with open(output_text_file, 'w', encoding='utf-8') as f:
        for message in filtered_data:
            f.write(message + '\n')

    print(f"Messages from '{specific_person}' copied to '{output_text_file}'.")

# Specify the CSV file and specific person
csv_file = 'sample_whatsapp_messages.csv'
specific_person = input("Whose messages do you want to copy? ")
output_text_file = 'read.txt'  # Change this to your desired output text file

# Call the function
copy_person_messages_to_text(csv_file, specific_person, output_text_file)
