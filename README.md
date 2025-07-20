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

## Project Structure
```text
matadata-exposed/
├── LICENCE              # This documentation file
├── README.md            # This documentation file
├── metadata_exposed.py  # Main script
```

## Contributing
Contributions are welcome! To contribute :
1. Fork the repository  
2. Create a feature branch (`git checkout -b feature/your-feature`)  
3. Commit your changes (`git commit -m 'Add new feature'`)  
4. Push to the branch (`git push origin feature/your-feature`)  
5. Open a Pull Request

## License
This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.
