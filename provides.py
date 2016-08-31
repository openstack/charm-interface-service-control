import uuid

from charms.reactive import hook
from charms.reactive import RelationBase
from charms.reactive import scopes


class NeutronControlProvides(RelationBase):
    scope = scopes.GLOBAL

    @hook('{provides:neutron-control}-relation-{joined,changed}')
    def changed(self):
        self.set_state('{relation_name}.connected')

    @hook('{provides:neutron-control}-relation-{broken,departed}')
    def broken(self):
        self.remove_state('{relation_name}.connected')

    def request_restart(self):
        conversation = self.conversation()
        relation_info = {
            'restart-trigger': str(uuid.uuid4()),
        }
        conversation.set_remote(**relation_info)
