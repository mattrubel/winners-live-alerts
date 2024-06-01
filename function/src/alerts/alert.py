import boto3


class Alert:

    def __init__(self, topic_arn: str):
        self.topic_arn = topic_arn

    def send_notification(self, subject: str, message: str):
        sns = boto3.client('sns')
        # https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sns/client/publish.html
        sns.publish(
            TopicArn=self.topic_arn,
            Message=message,
            Subject=subject,
            # MessageStructure="json",
        )
