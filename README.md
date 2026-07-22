# Steganography Tool

## Project Description
This Steganography Tool is an application designed to embed secret information within digital files, such as images or audio files, allowing users to securely transmit information without the risk of detection.

## Features
- **Hide Text in Images**: Embed text messages within images without noticeable changes to the image quality.
- **Extract Text from Images**: Retrieve hidden messages from steganographic images.
- **Support for Different Image Formats**: Works with common image formats such as JPEG and PNG.
- **User-Friendly Interface**: Simple and intuitive user interface for easy operation.

## Installation Instructions
1. **Clone the Repository**:
   ```bash
   git clone https://github.com/Anurag-singh6/steganography-tool.git
   ```
2. **Navigate to the Project Directory**:
   ```bash
   cd steganography-tool
   ```
3. **Install Dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

## Usage
- To hide a message in an image, run:
   ```bash
   python hide_message.py input_image.png "Your secret message here"
   ```
- To extract a message from an image, run:
   ```bash
   python extract_message.py input_image.png
   ```

## Technical Details
The tool uses algorithms based on the Least Significant Bit (LSB) method of steganography. This method modifies the least significant bits of the image's pixel data to embed the secret message. The tool is implemented in Python, utilizing libraries like PIL for image processing.

## Project Structure
```
steganography-tool/
│
├── hide_message.py           # Script to hide messages in images
├── extract_message.py        # Script to extract messages from images
├── requirements.txt          # Required libraries
└── README.md                # Project documentation
```
