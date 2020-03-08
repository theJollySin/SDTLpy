import requests
from pathlib import Path
from typing import Union

from .SDTLResult import SDTLResult


class SDTLClient:
    """
    To Add Script Files:
        Use either `add_directory` or `add_file` to add scripts to the client

    To send the SDTL request:
        Call `transform` to request the SDL for all of the files in the client

    To save the SDTL to Disk:
        To save the SDTL, call `save`
    """

    def __init__(self, endpoint_url: str):
        """
        Create the SDTL client. It needs to know which endpoint to use, so pass it in. This endpoint
        will be different for SASS and R.

        :param endpoint_url: The SDTL API endpoint
        """
        self.endpoint_url: str = endpoint_url
        self.results: SDTLResult = []
        self.input_files: Path = []
        self.input_directories: Path = []

    def add_file(self, file_path: Union[str, Path]) -> None:
        """
        Adds a file to the client.

        :param file_path: The path to the file
        :return: None
        """
        if isinstance(file_path, str):
            file_path = Path(file_path)
        self.input_files.append(file_path)

    def add_directory(self, directory_path: Union[str, Path]) -> None:
        """
        Adds a directory of files to the client.

        :param directory_path: The Path object representing a directory
        :return: None
        """
        if isinstance(directory_path, str):
            directory_path=Path(directory_path)
        self.input_directories.append(directory_path)

    def transform(self) -> None:
        """
        Takes the files and directories in the client and converts them into SDTL. The
        results are saved into Result objects.
        :return: None
        """
        for directory in self.directories:
            for file in directory.glob('**/*'):
                sdtl = self.get_sdtl(file)
                self.add_result(SDTLResult(sdtl, file))

        for file in self.input_files:
            sdtl = self.get_sdtl(file)
            self.add_result(SDTLResult(sdtl, file))

    def get_sdtl(self, file: Path) -> dict:
        """
        Gets the sdtl for a given file
        :param file: The file being transformed into SDTL
        :return: dict
        """
        params = {}
        data = {}
        r = requests.get(url=self.endpoint_url, params=params, data=data)
        return r.json()

    def add_result(self, sdtl, filename) -> None:
        result = SDTLResult(sdtl, filename)
        self.results.append(result)

    def save(self, directory_path: Union[Path, str]) -> None:
        for run in self.results:
            run.save(directory_path)

    def reset(self) -> None:
        """
        Resets the state of the client.
        :return:
        """
        pass