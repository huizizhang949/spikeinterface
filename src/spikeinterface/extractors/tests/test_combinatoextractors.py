import pytest


# from spikeinterface.extractors import read_combinato


@pytest.mark.skip("Combinato can be tested after running run_combinato()")
def test_combinatoextractors():
    # not tested here, tested in run_combinato(...)
    pass
    #  combinato_folder = '/home/samuel/Documents/SpikeInterface/spikeinterface/spikeinterface/sorters/tests/combinato_output/recording'
    #  sorting = read_combinato(combinato_folder)
    #  print(sorting)


if __name__ == "__main__":
    test_combinatoextractors()
