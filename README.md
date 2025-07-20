# Metadata Exposed

## Description

**Metadata Exposed** is a lightweight Python tool designed to get the more informations that we can get from a specific file.  
It will expose all the invisible data from a file in an orderly, structured way.

## Obtainable informations
- File name
- Absolute path
- Size
- Permissions
- MIME Type
- Encoding
- Creation date
- Last modification date
- Last opening date
- MD5
- SHA1
- SHA256
- EXIF
- Readable strings in the file

## Requirements
- Python 3.6 or higher  
- Python packages:
  - `os`  
  - `sys`
  - `stat`
  - `hashlib`
  - `mimetypes`
  - `requests`
  - `datetime`
  - `tempfile`
  - `chardet`
  - `time`
  - `colorama`

## Installation
Clone the repository or download the source files :
```bash
git clone https://github.com/V1ltrr/Metadata-Exposed.git
———
cd Metadata-Exposed
———
pip install requests os sys stat hashlib mimetypes datetime tempfile chardet time colorama
```
## Usage
Run the script by launching :
```bash
python metadata_exposed.py
```
### Steps
1. Select the fuzzing mode:  
   - Default built-in list  
   - Custom wordlist from `wordlist.txt`  
   - Exit the program
     
2. Select the display mode :  
   - Extended mode: view all tested URLs and their HTTP codes  
   - Reduced mode: view only a summary (200 & 403) with a progress bar
     
2. Enter the target URL:  
   - Must include the protocol (`http://` or `https://`)  
   - No spaces allowed  
   - Example: `https://example.com/admin`

## Project Structure
```text
url-breaker/
├── LICENCE              # This documentation file
├── README.md            # This documentation file
├── url_breaker.py       # Main script
├── wordlist.txt         # Optional custom variants file
```

## Internal Details

- Uses `requests` for HTTP requests.  
- URL variants are built using `urllib.parse.urljoin` to ensure valid URLs.  
- Handles network exceptions gracefully.  
- Uses `colorama` for colored terminal output.  
- Interactive CLI with `print()` and `input()` for user interaction.
- Uses concurrent.futures.ThreadPoolExecutor for concurrent requests.

## Limitations and Future Work

- Current fuzzing is based on a static list; future improvements could include dynamic variant generation.   
- Content comparison to detect significant differences between responses.  
- Exporting results to CSV or JSON.  
- Supporting other HTTP methods like POST or PUT.

## Contributing
Contributions are welcome! To contribute :
1. Fork the repository  
2. Create a feature branch (`git checkout -b feature/your-feature`)  
3. Commit your changes (`git commit -m 'Add new feature'`)  
4. Push to the branch (`git push origin feature/your-feature`)  
5. Open a Pull Request

## License
This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.
