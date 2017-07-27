import logging


led = {'name': 'LED Par',
       'channels': {'red': 0,
                    'green': 1,
                    'blue': 2,
                    'white': 3,
                    'control1': 4,
                    'control2': 5,
                    }
       }

rig = {'name': 'test',
       'fixtures': {
           'led1': {
               'address': 0,
               'device': led,
           },
           'led2': {
               'address': 7,
               'device': led,
           }
       },
       'groups': {
           'all': ['led1', 'led2'],
       }
       }

cue = {'led1': {'red': 127,
                'blue': 127,
                'green': 127,
                'white': 127,
                },
       'led2': {'green': 127,
                'yellow': 0,
                },
       'led3': {},
       }

cue_all = {'all': {'red': 127,
                   'blue': 127,
                   'green': 127,
                   'white': 127,
                   },
           }

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


class Rig:
    def __init__(self, description):
        self.name = description['name']
        self.fixtures = description['fixtures']
        self.groups = description.get('groups', {})
        self._process_fixtures()


    def _process_fixtures(self):
        self._fixtures = {}
        for id, fixture in self.fixtures.items():
            address = fixture['address']
            device = fixture['device']
            channels = device['channels']
            _fixture = {'id': id,
                        'device': device['name'],
                        'address': address,
                        'channels': {c: a + address for c, a in channels.items()}
                        }
            self._fixtures[id] = _fixture


    def _get_fixtures(self, fixture_or_group):
        if fixture_or_group in self.groups:
            return [self._fixtures[fixture] for fixture in self.groups[fixture_or_group]]
        elif fixture_or_group in self.fixtures:
            return [self._fixtures[fixture_or_group]]
        logger.warning("no fixture or group '{id}'".format(id=fixture_or_group))
        return []


    def evaluate_cue(self, cue):
        logger.info("evaluating cue")
        all_commands = []
        for fixture_name, commands in cue.items():
            fixtures = self._get_fixtures(fixture_name)
            for channel, value in commands.items():
                for fixture in fixtures:
                    try:
                        channel_address = fixture['channels'][channel]
                    except KeyError:
                        logger.warning("no channel '{channel}' for device '{id}'".format(channel=channel, id=fixture['id']))
                        continue
                    command = (channel_address, value)
                    all_commands.append(command)
        return all_commands


r = Rig(rig)

print(r.evaluate_cue(cue_all))
print(r.evaluate_cue(cue))