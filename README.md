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
* a empty directory for exporting

```bash
lina hide -d <SECRET FILE> -p <PASSWORD> -i <IMAGE DIR> -o <DIR FOR EXPORTING>
```

**reveal secret file from multiple png images**

These are required

* a directory containing png image files having secret file.

```bash
lina reveal -p <PASSWORD> -i <IMAGE DIR> -o <OUTPUT FILENAME>
```

### Contributing

Contributions are what make the open source community such an amazing place to learn, inspire, and create. Any contributions you make are greatly appreciated.

If you have a suggestion that would make this better, please fork the repo and create a pull request. You can also simply open an issue with the tag "enhancement". Don't forget to give the project a star! Thanks again!

1. Fork the Project
2. Create your Feature Branch (git checkout -b feature/AmazingFeature)
3. Commit your Changes (git commit -m 'Add some AmazingFeature')
4. Push to the Branch (git push origin feature/AmazingFeature)
5. Open a Pull Request


### LICENSE
MIT License
