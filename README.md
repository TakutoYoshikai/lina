# lina
<img src="./lina.png" width="400" alt="designed by Futa Takahashi">
lina is a steganography program. It can hide a binary file or a text file into multiple png images.

### Getting Started
**install**
```bash
pip install git+https://github.com/TakutoYoshikai/lina.git
```

**hide file into multiple png images**
```bash
lina hide -d <file> -p <password> -f <from IMAGE DIR> -t <to DIR>
```

**reveal file from multiple png images**
```bash
lina reveal -p <password> -f <from IMAGE DIR> -t <to OUTPUT FILE>
```

### LICENSE
MIT License
