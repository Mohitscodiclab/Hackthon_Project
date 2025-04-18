# 🛡️ PyRedact – Sensitive Data Redaction Tool in Python

PyRedact is a lightweight, Python-powered utility designed to automatically detect and redact sensitive information from text files. It ensures personal data privacy by scanning and masking content such as emails, phone numbers, credit card numbers, and social security numbers (SSNs).

---

## 📌 Features

- ✅ Detects and redacts:
  - Email addresses
  - Phone numbers (local & international)
  - Credit card numbers (Visa, MasterCard, AmEx, etc.)
  - Social Security Numbers (SSNs)
- ✅ Outputs a clean redacted file
- ✅ Generates a redaction log file with pattern-wise counts
- ✅ Easy to run and customize

---

## 💡 Inspiration

With data privacy becoming a major concern, the idea behind PyRedact was to build a simple, effective solution to protect sensitive information in text-based documents using Python. This project was built as part of a recruitment hackathon with real-world impact.

---

## 📚 What I Learned

- Crafting accurate regular expressions
- File handling in Python
- Writing scalable and modular code
- Importance of privacy and ethical software development

---

## 🧩 Challenges Faced

- Designing flexible regex patterns without false positives
- Handling various phone and card formats
- Maintaining the original readability of the redacted text
- Generating a meaningful and readable log

---

## 🛠️ Built With

- **Python 3** – Core programming language
- **Regular Expressions (`re` module)** – For detecting sensitive data
- **OS Module** – For file handling and saving outputs
- **Text Editor / IDE** – VS Code
- *(Optional for future use: AWS services for storage or processing)*

---

## 📂 Project Structure

```
PyRedact/
│
├── text.txt                 # Sample input file with sensitive data
├── redacted_output.txt     # Auto-generated output file with redacted data
├── redaction_log.txt       # Log file showing number of redactions per category
├── pyredact.py             # Main Python script
└── README.md               # This documentation file
```

---

## 🚀 How to Run

1. **Clone the repository**
   ```bash
   git clone https://github.com/mohitscodiclab/PyRedact.git
   cd PyRedact
   ```

2. **Make sure Python 3 is installed**
   ```bash
   python --version
   ```

3. **Run the script**
   ```bash
   python pyredact.py text.txt
   ```

4. **Check the outputs**
   - `redacted_output.txt` for the clean version
   - `redaction_log.txt` for the redaction summary

---

## 🧪 Sample Input (text.txt)

```
Hello Rohn,
Please contact me at rohn.wezzliy@example.com or at 749-418-483.
My card number is 5214 2352 4526 7485.
SSN: 382-64-4186
```

## ✅ Sample Output (redacted_output.txt)

```
Hello Rohn,
Please contact me at [REDACTED] or at [REDACTED].
My card number is [REDACTED].
SSN: [REDACTED]
```

---

## 📜 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

## 🙋‍♂️ Author

**Mohit Kumar**  
📍 West Bengal, India  
📧 mohit.email@example.com  
🔗 [LinkedIn](https://linkedin.com/in/yourprofile) | [GitHub](https://github.com/mohitscodiclab)

---

## 🌟 Show Your Support

If you found this project helpful, feel free to ⭐️ star the repo and contribute!


Let me know your **mohitscodiclab**, and I can even customize the links for you—or generate a `LICENSE` file too!
