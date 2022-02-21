import sys
from awsglue.utils import getResolvedOptions
from dpa.factory.config_factory import ConfigFactory
from dpa.job.validation_job import SparkValidationJob
# import uuid


args = getResolvedOptions(sys.argv, ['JOB_NAME'])
job_id = "23bebd3d-ed65-4ede-9729-fff233ab8a47"  # str(uuid.uuid4())
pipeline_manager_conn = 'dummy'

config_file_dir = 's3://gl-dpa-dqva/config'
cfn_config_file_path = f'{config_file_dir}/dpa_validation_config.yaml'


def run_glue_validate(config_file_path):
    # Read configuration and setup Spark Job
    config_factory = ConfigFactory()
    config = config_factory.get_config(config_file_path)
    job_name = args['JOB_NAME'] if args['JOB_NAME'] else config['job_name']
    config["connections"] = {}
    config["connections"]["pipeline_manager_conn"] = pipeline_manager_conn

    etl_job = SparkValidationJob(job_name, job_id, config)
    etl_job.run_job()
    etl_job.stop_spark()


run_glue_validate(cfn_config_file_path)
