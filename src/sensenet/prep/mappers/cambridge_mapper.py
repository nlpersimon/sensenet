import jsonlines
from .base_mapper import BaseMapper
from ...schema.sense_file import SenseFileLine


class CambridgeMapper(BaseMapper):
    SOURCE_NAME = 'cambridge'
    SOURCE_ABBREV = 'camb'

    def __init__(self,
                 sense_id: str = 'sense_id',
                 word: str = 'word',
                 pos: str = 'pos',
                 source: str = 'source',
                 definition: str = 'definition') -> None:
        super().__init__(
            sense_id=sense_id,
            word=word,
            pos=pos,
            source=source,
            definition=definition)

    def _read(self, file_pointer):
        assert isinstance(
            file_pointer, jsonlines.Reader), "Please use jsonlines to open the file"
        for line in file_pointer:
            yield line

    def get_word(self, raw_file_line) -> str:
        return raw_file_line['headword']

    def get_pos(self, raw_file_line) -> str:
        return raw_file_line['pos'] or 'null'

    def get_definition(self, raw_file_line) -> str:
        return raw_file_line['en_def']

    def get_source_abbrev(self) -> str:
        return self.SOURCE_ABBREV

    def get_source(self) -> str:
        return self.SOURCE_NAME
