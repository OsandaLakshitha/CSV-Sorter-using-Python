import pandas as pd
import os
import sys
from pathlib import Path

def create_directories():
    """Create source and output directories if they don't exist"""
    Path("source").mkdir(exist_ok=True)
    Path("output").mkdir(exist_ok=True)

def get_csv_files():
    """Get list of CSV files in source directory"""
    source_dir = Path("source")
    csv_files = list(source_dir.glob("*.csv"))
    return csv_files

def display_columns(df):
    """Display available columns with their index numbers"""
    print("\nAvailable columns:")
    for i, col in enumerate(df.columns, 1):
        print(f"{i}. {col}")

def get_sort_type():
    """Get sorting type from user"""
    while True:
        print("\nSelect sorting type:")
        print("1. Alphabetical (A-Z)")
        print("2. Alphabetical (Z-A)")
        print("3. Numerical (Low to High)")
        print("4. Numerical (High to Low)")
        
        choice = input("Enter your choice (1-4): ").strip()
        
        if choice == "1":
            return "alpha_asc"
        elif choice == "2":
            return "alpha_desc"
        elif choice == "3":
            return "num_asc"
        elif choice == "4":
            return "num_desc"
        else:
            print("Invalid choice. Please enter 1, 2, 3, or 4.")

def get_column_choice(df):
    """Get column choice from user"""
    while True:
        try:
            choice = int(input(f"\nSelect column to sort by (1-{len(df.columns)}): "))
            if 1 <= choice <= len(df.columns):
                return df.columns[choice - 1]
            else:
                print(f"Invalid choice. Please enter a number between 1 and {len(df.columns)}.")
        except ValueError:
            print("Please enter a valid number.")

def sort_dataframe(df, column, sort_type):
    """Sort dataframe based on specified column and sort type"""
    try:
        if sort_type == "alpha_asc":
            return df.sort_values(by=column, ascending=True, key=lambda x: x.astype(str).str.lower())
        elif sort_type == "alpha_desc":
            return df.sort_values(by=column, ascending=False, key=lambda x: x.astype(str).str.lower())
        elif sort_type == "num_asc":
            # Convert to numeric, errors='coerce' will turn non-numeric values to NaN
            df[column] = pd.to_numeric(df[column], errors='coerce')
            return df.sort_values(by=column, ascending=True)
        elif sort_type == "num_desc":
            df[column] = pd.to_numeric(df[column], errors='coerce')
            return df.sort_values(by=column, ascending=False)
    except Exception as e:
        print(f"Error sorting data: {e}")
        return None

def main():
    """Main function to run the CSV sorter"""
    print("=== CSV File Sorter ===")
    
    # Create directories
    create_directories()
    
    # Get CSV files
    csv_files = get_csv_files()
    
    if not csv_files:
        print("No CSV files found in the 'source' directory.")
        print("Please place your CSV files in the 'source' folder and run the program again.")
        return
    
    # Display available CSV files
    print(f"\nFound {len(csv_files)} CSV file(s):")
    for i, file in enumerate(csv_files, 1):
        print(f"{i}. {file.name}")
    
    # Get file selection
    while True:
        try:
            file_choice = int(input(f"\nSelect CSV file to sort (1-{len(csv_files)}): "))
            if 1 <= file_choice <= len(csv_files):
                selected_file = csv_files[file_choice - 1]
                break
            else:
                print(f"Invalid choice. Please enter a number between 1 and {len(csv_files)}.")
        except ValueError:
            print("Please enter a valid number.")
    
    # Read the CSV file
    try:
        print(f"\nReading {selected_file.name}...")
        df = pd.read_csv(selected_file)
        print(f"Successfully loaded {len(df)} rows and {len(df.columns)} columns.")
    except Exception as e:
        print(f"Error reading CSV file: {e}")
        return
    
    # Display columns
    display_columns(df)
    
    # Get column choice
    column_to_sort = get_column_choice(df)
    
    # Get sort type
    sort_type = get_sort_type()
    
    # Sort the dataframe
    print(f"\nSorting by column '{column_to_sort}'...")
    sorted_df = sort_dataframe(df.copy(), column_to_sort, sort_type)
    
    if sorted_df is None:
        print("Failed to sort the data. Please check your data and try again.")
        return
    
    # Generate output filename
    base_name = selected_file.stem
    sort_desc = {
        "alpha_asc": "alpha_asc",
        "alpha_desc": "alpha_desc", 
        "num_asc": "num_asc",
        "num_desc": "num_desc"
    }
    
    output_filename = f"{base_name}_sorted_{column_to_sort}_{sort_desc[sort_type]}.csv"
    output_path = Path("output") / output_filename
    
    # Save sorted data
    try:
        sorted_df.to_csv(output_path, index=False)
        print(f"\nSorted file saved as: {output_path}")
        print("Operation completed successfully!")
    except Exception as e:
        print(f"Error saving file: {e}")

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n\nProgram interrupted by user.")
    except Exception as e:
        print(f"\nUnexpected error: {e}")
    
    input("\nPress Enter to exit...")