from rally import consts
from rally.plugins.openstack import scenario
from rally.plugins.openstack.scenarios.magnum import utils
from rally.plugins.openstack.scenarios.nova import utils as nova_utils
from rally.task import validation

@validation.add("required_services", services=[consts.Service.MAGNUM])
@validation.add("required_platform", platform="openstack", users=True)
@scenario.configure(
    context={"cleanup@openstack": ["magnum.clusters", "nova.keypairs"]},
    name="ScenarioPlugin.create_and_delete_magnum_clusters",
    platform="openstack")

class CreateAndDeleteClusters(utils.MagnumScenario):

   def run(self, node_count, **kwargs):
        """create cluster and then delete.
    :param node_count: the cluster node count.
    :param cluster_template_uuid: optional, if user want to use an existing cluster_template
    :param force_delete: force delete cluster if set to True
    :param kwargs: optional additional arguments for cluster creation
        """
        cluster_template_uuid = kwargs.get("cluster_template_uuid", None)
        if cluster_template_uuid is None:
            cluster_template_uuid = self.context["tenant"]["cluster_template"]
        else:
            del kwargs["cluster_template_uuid"]

        nova_scenario = nova_utils.NovaScenario({
            "user": self.context["user"],
            "task": self.context["task"],
            "config": {"api_versions": self.context["config"].get(
                "api_versions", [])}
        })
        keypair = nova_scenario._create_keypair()

 new_cluster = self._create_cluster(cluster_template_uuid, node_count, keypair=keypair, **kwargs)
        self.assertTrue(new_cluster, "Failed to create new cluster")

 self.delete_cluster(new_cluster, force=force_delete)
        self.assertIn(new_cluster.uuid, "Cluster cannot be found and deleted")
