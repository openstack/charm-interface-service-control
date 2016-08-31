import uuid

from charms.reactive import hook
from charms.reactive import RelationBase
from charms.reactive import scopes


class ServiceControlRequires(RelationBase):
    scope = scopes.GLOBAL

    @hook('{requires:service-control}-relation-{joined,changed}')
    def changed(self):
        self.set_state('{relation_name}.connected')

    @hook('{requires:service-control}-relation-{broken,departed}')
    def broken(self):
        self.remove_state('{relation_name}.connected')

    def request_restart(self, service_type=None):
        """Request a restart of a set of remote services

        :param service_type: string Service types to be restarted eg 'neutron'.
                                    If ommitted a request to restart all
                                    services is sent
        """
        conversation = self.conversation()
        if service_type:
            key = 'restart-trigger-{}'.format(service_type)
        else:
            key = 'restart-trigger'
        relation_info = {
            key: str(uuid.uuid4()),
        }
        conversation.set_remote(**relation_info)
