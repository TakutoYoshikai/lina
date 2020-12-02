# lina
<img src="./lina.png" width="400" alt="designed by Futa Takahashi">
lina is a steganography program. It can hide a binary file or a text file into multiple png images.

### Getting Started
**install**
```bash
pip3 install -r requirements.txt
```

**hide file into multiple png images**
```bash
python3 lina.py hide -d <file> -p <password> -f <from DIR> -t <to DIR>
```

**reveal file from multiple png images**
```bash
python3 lina.py reveal -p <password> -f <from DIR> -t <to OUTPUT FILE>
```
