from charms.reactive import RelationBase
from charms.reactive import hook
from charms.reactive import scopes


class MuninRequires(RelationBase):
    scope = scopes.GLOBAL

    # These remote data fields will be automatically mapped to accessors
    # with a basic documentation string provided.
    auto_accessors = ['access-network', 'db_host',
                      'ssl_ca', 'ssl_cert', 'ssl_key']

    @hook('{requires:munin}-relation-joined')
    def joined(self):
        self.set_state('{relation_name}.relation.joined')

    @hook('{requires:munin}-relation-changed')
    def changed(self):
        self.set_state('{relation_name}.available')

    @hook('{requires:munin}-relation-{broken,departed}')
    def departed(self):
        self.remove_state('{relation_name}.available')
