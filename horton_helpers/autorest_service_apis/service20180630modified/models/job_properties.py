# coding=utf-8
# --------------------------------------------------------------------------
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.serialization import Model


class JobProperties(Model):
    """JobProperties.

    :param job_id: System generated.  Ignored at creation.
    :type job_id: str
    :param start_time_utc: System generated.  Ignored at creation.
    :type start_time_utc: datetime
    :param end_time_utc: System generated.  Ignored at creation.
     Represents the time the job stopped processing.
    :type end_time_utc: datetime
    :param type: Required.
     The type of job to execute. Possible values include: 'unknown', 'export',
     'import', 'backup', 'readDeviceProperties', 'writeDeviceProperties',
     'updateDeviceConfiguration', 'rebootDevice', 'factoryResetDevice',
     'firmwareUpdate', 'scheduleDeviceMethod', 'scheduleUpdateTwin',
     'restoreFromBackup', 'failoverDataCopy'
    :type type: str or ~service20180630modified.models.enum
    :param status: System generated.  Ignored at creation. Possible values
     include: 'unknown', 'enqueued', 'running', 'completed', 'failed',
     'cancelled', 'scheduled', 'queued'
    :type status: str or ~service20180630modified.models.enum
    :param progress: System generated.  Ignored at creation.
     Represents the percentage of completion.
    :type progress: int
    :param input_blob_container_uri: URI containing SAS token to a blob
     container that contains registry data to sync.
    :type input_blob_container_uri: str
    :param input_blob_name: The blob name to be used when importing from the
     provided input blob container.
    :type input_blob_name: str
    :param output_blob_container_uri: URI containing SAS token to a blob
     container.  This is used to output the status of the job and the results.
    :type output_blob_container_uri: str
    :param output_blob_name: The name of the blob that will be created in the
     provided output blob container.  This blob will contain
     the exported device registry information for the IoT Hub.
    :type output_blob_name: str
    :param exclude_keys_in_export: Optional for export jobs; ignored for other
     jobs.  Default: false.  If false, authorization keys are included
     in export output.  Keys are exported as null otherwise.
    :type exclude_keys_in_export: bool
    :param failure_reason: System genereated.  Ignored at creation.
     If status == failure, this represents a string containing the reason.
    :type failure_reason: str
    """

    _attribute_map = {
        'job_id': {'key': 'jobId', 'type': 'str'},
        'start_time_utc': {'key': 'startTimeUtc', 'type': 'iso-8601'},
        'end_time_utc': {'key': 'endTimeUtc', 'type': 'iso-8601'},
        'type': {'key': 'type', 'type': 'str'},
        'status': {'key': 'status', 'type': 'str'},
        'progress': {'key': 'progress', 'type': 'int'},
        'input_blob_container_uri': {'key': 'inputBlobContainerUri', 'type': 'str'},
        'input_blob_name': {'key': 'inputBlobName', 'type': 'str'},
        'output_blob_container_uri': {'key': 'outputBlobContainerUri', 'type': 'str'},
        'output_blob_name': {'key': 'outputBlobName', 'type': 'str'},
        'exclude_keys_in_export': {'key': 'excludeKeysInExport', 'type': 'bool'},
        'failure_reason': {'key': 'failureReason', 'type': 'str'},
    }

    def __init__(self, job_id=None, start_time_utc=None, end_time_utc=None, type=None, status=None, progress=None, input_blob_container_uri=None, input_blob_name=None, output_blob_container_uri=None, output_blob_name=None, exclude_keys_in_export=None, failure_reason=None):
        super(JobProperties, self).__init__()
        self.job_id = job_id
        self.start_time_utc = start_time_utc
        self.end_time_utc = end_time_utc
        self.type = type
        self.status = status
        self.progress = progress
        self.input_blob_container_uri = input_blob_container_uri
        self.input_blob_name = input_blob_name
        self.output_blob_container_uri = output_blob_container_uri
        self.output_blob_name = output_blob_name
        self.exclude_keys_in_export = exclude_keys_in_export
        self.failure_reason = failure_reason
