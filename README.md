# lina
<img src="./lina.png" width="400">
lina is a steganography program. It can hide a binary file or a text file into multiple png images.

### Getting Started
```bash
pip3 install -r requirements.txt
```

hide file into multiple png images
```bash
python lina.py hide -d <file> -p <password> -f <from DIR> -t <to DIR>
```

reveal file from multiple png images
```bash
python lina.py reveal -p <password> -f <from DIR> -t <to OUTPUT FILE>
```
