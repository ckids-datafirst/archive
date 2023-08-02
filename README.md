# DataFestArchive - Generate DataFestArchive Website

DataFestArchive is a Python package designed to generate the DataFestArchive website from past versions of DataFest. It reads project information from a provided database and automatically generates the required web pages to showcase these projects.

## Database

The database schema for storing DataFest project information is available at [link to file](https://example.com/path/to/database/schema).

## How to Use

1. Install DataFestArchive using `setup.py`:

```bash
python setup.py install
```

2. Generate the DataFestArchive website:

To generate the website, run the `datafestarchive` command, followed by the path to your database file and the target directory for the website:

```bash
python setup.py install
```

Replace `[data/datafest.sql]` with the path to your database file containing DataFest project information. The database should adhere to the specified schema.

Replace `[website]` with the target directory where the generated website should be saved.

3. Access the Generated Website:

Once the process is complete, you will find the generated DataFestArchive website in the specified `[website]` directory.

## Contributing

We welcome contributions to improve DataFestArchive! If you find any issues or have suggestions for enhancements, please feel free to open an issue or submit a pull request.

## License

This project is licensed under the [MIT License](LICENSE).
