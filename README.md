# FILE-INTEGRITY-CHECKER

### COMPANY   : Codtech IT Solutions

### NAME      : Alla Meghana Reddy

### INTERN ID : CT06DG1638

### DOMAIN    : Cyber Security & Ethical Hacking

### DURATION  : 6 weeks

### MENTOR    : Neela Santhosh

### DESCRIPTION OF TASK: 

TASK NAME - File Integrity Checker using Python Code

GOAL      - The primary objective of this task was to design and implement a File Integrity Checker, a cybersecurity utility that scans directories and monitors file changes             by computing and comparing cryptographic hash values. This process—known as hashing—assigns each file a unique digital fingerprint. Every time the script is run,             it compares the latest hash values against previously stored values to detect:
                                                                                          - Unauthorized or accidental modifications
                                                                                          - Newly added files
                                                                                          - Deleted files
           By doing this, the tool enables users to monitor file integrity in a clear, fast, and automated manner. This project demonstrates a foundational cybersecurity                principle: maintaining the integrity of digital assets.

PLATFORMS USED - The development of the task was carried out using Visual Studio Code as the IDE, offering a flexible coding space with Python support and Git                                 integration. The final script is version-controlled and publicly accessible via a GitHub repository, allowing for collaborative feedback  and potential                       community improvements.

TOOLS AND TECHNOLOGIES - 1. Python : The high-level programming language due to its clarity, rich libraries, and ease of use.
                         2. hashlib : A built-in python module that provides access to secure hash algorithms such as SHA-256. This is used to generate cryptographic 
                                        hashes for files.
                         3. os : Utilized for directory traversal and interaction with the filesystem, enabling the script to recursively check all files in a specified                                       folder.
                         4. json : Used to serialize and store the hash records in a persistent .json format, maintaining a state between different runs of the script.
                         5. Github : The completed tasks are stored in the repositoty. 
                         6. tqdm – Displays real-time progress bars during file scanning.
                         7. colorama – Enables cross-platform colored text output in the terminal.
                         8. rich – Used for creating modern, visually appealing CLI elements like tables and panels.
                         
 FUNCTIONALITY - The script executes the following steps:
                 1. Directory Scanning – Recursively walks through the user-specified directory, collecting eligible files while skipping known temp/system folders.
                 2. Hash Generation – Computes SHA-256 hashes for all scanned files.
                 3. State Comparison – Compares the current hash values with previously saved data to detect: New Files – Added since the last run
                                                                                                              Modified Files – Changed content (detected by mismatched hashes)
                                                                                                              Deleted Files – No longer present in the scanned folder
                 4. Logging – All detected changes are logged in a plain text log file for review.
                 5. Summary Report – After scanning, a color-coded and boxed summary is displayed, showing the number of new, modified, and deleted files.
                 6. Progress Bar – Gives visual feedback as the scan progresses.
                 7. Optional Input – Supports command-line arguments or interactive input for flexibility

APPLICATIONS OT THE TASK -
                          1. Cybersecurity - Integrity monitoring is a crucial component of host-based intrusion detection systems (HIDS). This script provides foundational                               exposure to such practices.
                          2. Digital Forensics - can use this tool during post-incident investigations to verify whether critical logs or executable files were tampered with.
                          3. Compliance - Organizations bound by security standards like ISO 27001, PCI-DSS, or HIPAA need to ensure the integrity of sensitive files. This                                tool can be adapted into compliance audits.
                          4. Backup Verification - Ensuring that backed-up files have not been inadvertently corrupted or altered during storage or transfer.
                          5. Software Development - Developers can use this tool to verify that their deployments or builds are unaltered from verified source files.

#### OUTPUT - 

![Image](https://github.com/user-attachments/assets/65b08a03-961d-438e-9078-e9a827ec98c3)


