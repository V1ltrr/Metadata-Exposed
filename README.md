<h1 align="center">  Metadata Exposed </h1>

<p align="center">
  <img src="https://img.shields.io/badge/Version-0.1-green?style=for-the-badge">
  <img src="https://img.shields.io/github/license/v1ltrr/Metadata-Exposed?style=for-the-badge">
  <img src="https://img.shields.io/github/stars/v1ltrr/Metadata-Exposed?style=for-the-badge">
  <img src="https://img.shields.io/github/issues/v1ltrr/Metadata-Exposed?color=red&style=for-the-badge">
  <img src="https://img.shields.io/github/forks/v1ltrr/Metadata-Exposed?color=teal&style=for-the-badge">
</p>

<p align="center">
  <img src="https://img.shields.io/badge/Author-v1ltrr-blue?style=flat-square">
  <img src="https://img.shields.io/badge/Open%20Source-Yes-darkgreen?style=flat-square">
  <img src="https://img.shields.io/badge/Maintained%3F-Yes-lightblue?style=flat-square">
  <img src="https://img.shields.io/badge/Written%20In-Python-darkcyan?style=flat-square">
</p>

---

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
