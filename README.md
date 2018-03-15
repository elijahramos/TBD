# TBD
Okay, I did even more polishing. so I realized that if MyfileEncrypt did not have file IO routines the whole module was basically redundant, so I left them in. the jist behind it now is that is basically Myencrypt but it can take a filePath for a parameter. the inverse for MyfileEncrypt however does work, but its unused in the test.py. It takes a file that has the RAW cipher text from the norm() and deciphers it with the key. the test.py has it so that the ciphertext is bundled with the IV, RSA encrypted key, and the file's extention. Because of this, calling MyfileEncrypt's inverse is unneeded, and instead Myencrypt's inverse is used.

Anyway, the program is extra shiny now, and pretty much satisfies the expected outcome of the lab, AT LEAST to a reasonable extent.
