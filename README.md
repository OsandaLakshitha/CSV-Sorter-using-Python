# CSV Sorter 📊

A powerful and user-friendly Python application for sorting CSV files with multiple sorting options and an intuitive command-line interface.

![Python](https://img.shields.io/badge/python-v3.7+-blue.svg)
![License](https://img.shields.io/badge/license-MIT-green.svg)
![Platform](https://img.shields.io/badge/platform-windows%20%7C%20macOS%20%7C%20linux-lightgrey.svg)

## ✨ Features

- **Multiple Sorting Options**: Alphabetical (A-Z, Z-A) and Numerical (Low-High, High-Low)
- **Interactive Column Selection**: Choose any column from your CSV file
- **Batch Processing Ready**: Handle multiple CSV files in sequence
- **Smart File Management**: Organized source and output folder structure
- **Error Handling**: Robust error handling for common data issues
- **Cross-Platform**: Works on Windows, macOS, and Linux
- **Executable Version**: Convert to standalone .exe for easy distribution

## 🚀 Quick Start

### Prerequisites

- Python 3.7 or higher
- pip (Python package installer)

### Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/OsandaLakshitha/CSV-Sorter-using-Python.git
   cd csv-sorter
   ```

2. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```
   
   Or install pandas directly:
   ```bash
   pip install pandas
   ```

3. **Run the application:**
   ```bash
   python CSVSorter.py
   ```

## 📁 Project Structure

```
CSV-Sorter-using-Python/
│
├── CSVSorter.py          # Main application
├── requirements.txt       # Python dependencies
├── README.md             # Project documentation
├── LICENSE               # MIT License
├── source/               # Place your CSV files here
├── output/               # Sorted files appear here
└── examples/             # Sample CSV files for testing
    ├── sample_data.csv
    └── employee_data.csv
```

## 🎯 Usage

### Basic Usage

1. **Place your CSV files** in the `source/` directory
2. **Run the program:**
   ```bash
   python CSVSorter.py
   ```
3. **Follow the interactive prompts:**
   - Select your CSV file
   - Choose the column to sort by
   - Pick your sorting method
4. **Find your sorted file** in the `output/` directory

### Example Workflow

```
=== CSV File Sorter ===

Found 2 CSV file(s):
1. employees.csv
2. sales_data.csv

Select CSV file to sort (1-2): 1

Successfully loaded 150 rows and 5 columns.

Available columns:
1. Name
2. Department
3. Salary
4. Years_Experience
5. Performance_Score

Select column to sort by (1-5): 3

Select sorting type:
1. Alphabetical (A-Z)
2. Alphabetical (Z-A)
3. Numerical (Low to High)
4. Numerical (High to Low)

Enter your choice (1-4): 4

Sorting by column 'Salary'...
Sorted file saved as: output/employees_sorted_Salary_num_desc.csv
Operation completed successfully!
```

## 🔧 Building Executable

Create a standalone executable that doesn't require Python installation:

### Using PyInstaller

1. **Install PyInstaller:**
   ```bash
   pip install pyinstaller
   ```

2. **Create executable:**
   ```bash
   pyinstaller --onefile --console --name "CSVSorter" CSVSorter.py
   ```

3. **Find your executable:**
   - Located in `dist/CSVSorter.exe` (Windows)
   - Ready for distribution!

### Alternative: Using auto-py-to-exe (GUI)

```bash
pip install auto-py-to-exe
auto-py-to-exe
```

## 📊 Supported Data Types

- **Text Data**: Names, categories, descriptions
- **Numerical Data**: Integers, decimals, financial data
- **Mixed Data**: Automatically handles mixed column types
- **Large Files**: Efficiently processes files with thousands of rows

## 🛠️ Advanced Features

### Custom Sorting Options

The application intelligently handles:
- **Case-insensitive alphabetical sorting**
- **Automatic numeric type conversion**
- **Missing data handling** (NaN values sorted to end)
- **Mixed data type columns**

### Output File Naming

Files are automatically named with descriptive suffixes:
- `original_sorted_ColumnName_alpha_asc.csv`
- `original_sorted_ColumnName_num_desc.csv`

## 🤝 Contributing

We welcome contributions! Here's how you can help:

1. **Fork the repository**
2. **Create a feature branch:**
   ```bash
   git checkout -b feature/amazing-feature
   ```
3. **Commit your changes:**
   ```bash
   git commit -m 'Add amazing feature'
   ```
4. **Push to the branch:**
   ```bash
   git push origin feature/amazing-feature
   ```
5. **Open a Pull Request**

### Development Setup

```bash
# Clone your fork
git clone https://github.com/yourusername/csv-sorter.git

# Create virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Run tests (if available)
python -m pytest
```

## 🐛 Issue Reporting

Found a bug? Have a feature request? Please check our [Issues](https://github.com/yourusername/csv-sorter/issues) page.

**When reporting issues, please include:**
- Operating system and version
- Python version
- Sample CSV file (if possible)
- Error messages or screenshots

## 📋 Requirements

- **Python**: 3.7+
- **pandas**: 1.3.0+
- **pathlib**: Built-in (Python 3.4+)

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- Built with [pandas](https://pandas.pydata.org/) for robust data manipulation
- [PyInstaller](https://www.pyinstaller.org/) for executable creation
- Inspired by the need for simple, efficient CSV processing tools

## 📞 Support

- **Documentation**: Check this README and inline code comments
- **Issues**: [GitHub Issues](https://github.com/OsandaLakshitha/CSV-Sorter-using-Python/issues)
- **Discussions**: [GitHub Discussions](https://github.com/Osandalakshitha/CSV-Sorter-Using-Python/discussions)

## 🗺️ Roadmap

- [ ] GUI version using tkinter
- [ ] Support for Excel files (.xlsx, .xls)
- [ ] Multiple column sorting
- [ ] Custom delimiter support
- [ ] Data preview before sorting
- [ ] Undo functionality
- [ ] Batch processing improvements

---

**⭐ If you found this project helpful, please give it a star!**

*Made with ❤️ for the data processing community*