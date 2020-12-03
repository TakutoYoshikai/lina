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
lina hide -d <file> -p <password> -i <input IMAGE DIR> -o <output DIR>
```

**reveal secret file from multiple png images**
```bash
lina reveal -p <password> -i <input IMAGE DIR> -o <output FILENAME>
```

### LICENSE
MIT License
