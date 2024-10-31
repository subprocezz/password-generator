# Password Generator

## Overview

The Password Generator is a command-line application written in Python that creates strong, random passwords based on user-defined criteria. This project emphasizes the importance of using secure passwords for online accounts.

## Features

- **Customizable Length**: Users can specify the desired length of the password.
- **Character Type Options**:
  - Include uppercase letters
  - Include lowercase letters
  - Include numbers
  - Include special characters
- **Random Password Generation**: Generates a secure random password based on the selected options.

## Installation

1. Ensure you have Python installed on your system.
2. Clone or download the repository.

```bash
git clone https://github.com/subprocezz/password-generator
```

3. Navigate to the project directory
```
cd password-generator
```

Usage

Run the script using the following command format:

bash

python generador_contrasenas.py -l LENGTH [-u] [-lc] [-n] [-s]

Arguments

    -l or --length: Required. Specifies the length of the password (integer).
    -u or --include_upper: Optional. Includes uppercase letters in the password.
    -lc or --include_lower: Optional. Includes lowercase letters in the password.
    -n or --include_numbers: Optional. Includes numbers in the password.
    -s or --include_special: Optional. Includes special characters in the password.

Example

To generate a password of length 12 that includes uppercase letters, lowercase letters, numbers, and special characters:

bash

python generador_contrasenas.py -l 12 -u -lc -n -s

Code Structure

    get_character_set(include_upper, include_lower, include_numbers, include_special): Constructs the character set based on user preferences.
    generate_password(length, character_set): Generates a random password using the specified length and character set.
    main(): Handles user input, parses command-line arguments, and prints the generated password.

License

This project is open-source and available for personal use and modification.
Contributing

Feel free to contribute to the project by submitting issues or pull requests. Your contributions are welcome!
Acknowledgments

    Python community for providing the argparse and random modules.
    Inspiration from various online password generation tools.

vbnet


### How to Use the Documentation

1. Save the above content in a file named `README.md` in your project directory.
2. You can view this documentation using any Markdown viewer or by uploading it to platforms like GitHub, where it will render automatically.

Let me know if you need any additional information!

