import pathlib

from pydiggs.boringlog import BoringLog

def export_log():
    samples_dir = pathlib.Path(__file__).parents[1].joinpath('data', 'samples')
    sample_file = samples_dir.joinpath('600304_20180702.xml')
    log = BoringLog()
    log.extract_xml(sample_file)
    log.to_pdf(r'C:\Temp\BoringLog.pdf')

if __name__ == '__main__':
    export_log()
