# Import necessary libraries
import pandas as pd  # For data manipulation and analysis
from fpdf import FPDF  # For generating PDF reports

# Function to collect user input for Sales, Expenses, and Profit
def collect_user_data():
    data = []  # List to store user input
    print("Enter Sales, Expenses, and Profit for each entry. Type 'done' to finish.")
    while True:
        # Ask the user for Sales input
        sales = input("Enter Sales (or 'done' to finish): ")
        if sales.lower() == 'done':  # Exit the loop if the user types 'done'
            break
        # Ask the user for Expenses and Profit inputs
        expenses = input("Enter Expenses: ")
        profit = input("Enter Profit: ")
        try:
            # Convert inputs to float (numeric values)
            sales = float(sales)
            expenses = float(expenses)
            profit = float(profit)
            # Append the data as a list to the main data list
            data.append([sales, expenses, profit])
        except ValueError:  # Handle invalid (non-numeric) input
            print("Invalid input. Please enter numeric values.")
    return data  # Return the collected data

# Function to save the collected data to a CSV file
def save_data_to_csv(data, file_path="data.csv"):
    # Convert the list of data into a pandas DataFrame
    df = pd.DataFrame(data, columns=["Sales", "Expenses", "Profit"])
    # Save the DataFrame to a CSV file
    df.to_csv(file_path, index=False)
    print(f"Data saved to {file_path}")

# Function to analyze the data
def analyze_data(data):
    # Perform basic statistical analysis on the data
    analysis_results = {
        'mean': data.mean(),  # Calculate the mean of each column
        'max': data.max(),    # Calculate the maximum value of each column
        'min': data.min(),    # Calculate the minimum value of each column
        'std_dev': data.std() # Calculate the standard deviation of each column
    }
    return analysis_results  # Return the analysis results

# Function to generate a PDF report from the analysis results
def generate_pdf_report(analysis_results, output_file="report.pdf"):
    pdf = FPDF()  # Create a new PDF object
    pdf.add_page()  # Add a page to the PDF
    pdf.set_font("Arial", size=12)  # Set the font and size for the title

    # Add a title to the PDF
    pdf.cell(200, 10, txt="Data Analysis Report", ln=True, align="C")

    # Add analysis results to the PDF
    pdf.ln(10)  # Add a line break
    pdf.set_font("Arial", size=10)  # Set the font and size for the results
    for key, value in analysis_results.items():
        # Add each analysis result to the PDF
        pdf.cell(200, 10, txt=f"{key}: {value}", ln=True)

    # Save the PDF to the specified output file
    pdf.output(output_file)

# Main function to tie everything together
def main():
    file_path = "data.csv"  # Path to the CSV file

    # Step 1: Collect user input
    data = collect_user_data()

    # Step 2: Save the collected data to a CSV file
    save_data_to_csv(data, file_path)

    # Step 3: Read the data from the CSV file into a pandas DataFrame
    data = pd.read_csv(file_path)

    # Step 4: Analyze the data
    analysis_results = analyze_data(data)

    # Step 5: Generate a PDF report from the analysis results
    generate_pdf_report(analysis_results)

    # Notify the user that the report has been generated
    print(f"Report generated successfully: report.pdf")

# Entry point of the script
if __name__ == "__main__":
    main()  # Call the main function to run the script