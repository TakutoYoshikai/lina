# lina
<img src="./lina.png" width="400" alt="designed by Futa Takahashi">
lina is a steganography program. It can hide a binary file or a text file into multiple png images.

### Getting Started
**install**
```bash
pip install git+https://github.com/TakutoYoshikai/lina.git
```

**hide file into multiple png images**

These are required

* a secret file to hide
* a directory containing png image files
* a directory(destination)

```bash
lina hide -d <SECRET FILE> -p <PASSWORD> -i <IMAGE DIR> -o <DESTINATION DIR>
```

**reveal secret file from multiple png images**

These are required

* a directory containing png image files having secret file.

```bash
lina reveal -p <PASSWORD> -i <input IMAGE DIR> -o <OUTPUT FILENAME>
```

### LICENSE
MIT License
