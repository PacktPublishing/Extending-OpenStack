from neutron.plugins.ml2 import driver_api as api
from neutron.db import api as db_api
from oslo_log import log as pp_logger
LOG = pp_logger.getLogger(__name__)

class MyExtDriver(api.MechanismDriver):

    def initialize(self):
  LOG.info("Initializing MyExtDriver driver ")

def create_port_precommit(self, context):
       port = context.current
       network = context.network
       LOG.info(“Create Network Port Precommits with associated network: %s ” %(network.current['name']))

def create_port_postcommit(self, context):
       port = context.current
       network = context.network
       LOG.info(“Create Network Port Postcommits with associated network: %s ” %(network.current['name']))

def delete_port_precommit(self, context):
       port = context.current
       LOG.info(“Delete Network Port Precommits with associated network: %s ” %(network.current['name']))

def delete_port_postcommit(self, context):
       port = context.current
       network = context.network
       LOG.info(“Delete Network Port Postcommits with associated network: %s ” %(network.current['name']))

def update_port_precommit(self, context):
       port = context.current
       network = context.network
       LOG.info(“Update Network Port Precommits with associated network: %s ” %(network.current['name']))

def update_port_postcommit(self, context):
       port = context.current
       network = context.network
       LOG.info(“Update Network Port Postcommits with associated network: %s ” %(network.current['name']))
