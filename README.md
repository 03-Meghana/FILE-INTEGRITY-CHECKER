# FILE-INTEGRITY-CHECKER

Company   : Codtech IT Solutions

Name      : Alla Meghana Reddy

Intern ID : CT06DG1638

Domain    : Cyber Security & Ethical Hacking

Duration  : 6 weeks

Mentor    : Neela Santhosh

Descrition of Task-1 : 
--> Task Name - File Integrity Checker using Python Code
--> Goal      - The primary goal of this task was to design and implement a File Integrity Checker—a cybersecurity utility that monitors changes to files by calculating and                  comparing hash values. It is possible by using the method called "hashing", which gives each file a unique digital fingerprint. By comparing these                            fingerprints each time the tool runs, we can see if something in the files has been modified—either on purpose or by accident. This task has the basics of                    how to keep files safe and identify any unwanted changes, which is a key part of cybersecurity.
--> Platforms used - The development of the task was carried out using Visual Studio Code as the IDE, offering a flexible coding space with Python support and Git                                 integration. The final script is version-controlled and publicly accessible via a GitHub repository, allowing for collaborative feedback  and potential                       community improvements.
--> Tools & Technologies - 1. Python : The high-level programming language due to its clarity, rich libraries, and ease of use.
                           2. hashlib : A built-in python module that provides access to secure hash algorithms such as SHA-256. This is used to generate cryptographic 
                                        hashes for files.
                           3. os : Utilized for directory traversal and interaction with the filesystem, enabling the script to recursively check all files in a specified                                       folder.
                           4. json : Used to serialize and store the hash records in a persistent .json format, maintaining a state between different runs of the script.
                           5. Github : The completed tasks are stored in the repositoty. 
--> Functionality Overview - The script works by first scanning a user-specified directory and computing SHA-256 hashes for all files. These hashes are stored in a                                        file_hashes.json file. On subsequent executions, the script compares the current state of the directory to the previously recorded hashes to                                  detect:
                                    - New files – Indicating files that have been added since the last scan.
                                    - Modified files – Where the current hash differs from the stored one, suggesting the file has changed.
                                    - Deleted files – Files that existed during the last run but are now missing.
                             This allows the user to monitor file integrity in a clear, automated manner, receiving alerts on any detected inconsistencies.
--> Applications of This Task:
                          1. Cybersecurity - Integrity monitoring is a crucial component of host-based intrusion detection systems (HIDS). This script provides foundational                               exposure to such practices.
                          2. Digital Forensics - can use this tool during post-incident investigations to verify whether critical logs or executable files were tampered with.
                          3. Compliance - Organizations bound by security standards like ISO 27001, PCI-DSS, or HIPAA need to ensure the integrity of sensitive files. This                                tool can be adapted into compliance audits.
                          4.Backup Verification - Ensuring that backed-up files have not been inadvertently corrupted or altered during storage or transfer.
                          5. Software Development - Developers can use this tool to verify that their deployments or builds are unaltered from verified source files.



