import pytest

from rasa_nlu.trainers.mitie_trainer import MITIETrainer
from rasa_nlu.train import load_configuration

class TestMitieTrainer:
    def test_failure_on_invalid_lang(self):
        config = load_configuration("config_example.json")
        with pytest.raises(NotImplementedError):
            MITIETrainer(config['backends']['mitie'], 'umpalumpa')
