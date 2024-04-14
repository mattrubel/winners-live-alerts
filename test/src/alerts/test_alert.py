import pytest
from unittest.mock import MagicMock, patch
from src.alerts.alert import Alert


class TestAlert:
    obj = Alert("test-topic")

    def test_alert(self):
        assert self.obj.topic_arn == "test-topic"

    @pytest.fixture
    def sns_client_mock(self):
        with patch('boto3.client') as boto3_client_mock:
            yield boto3_client_mock.return_value

    def test_send_notification(self, sns_client_mock):
        # Mock the response of the publish method
        sns_client_mock.publish = MagicMock(return_value={'MessageId': '123'})

        # Call the function that sends the SNS notification
        self.obj.send_notification('test-sub', 'test-msg')

        # Verify that the publish method was called with the correct parameters
        sns_client_mock.publish.assert_called_once_with(
            TopicArn='test-topic',
            Message='test-msg',
            Subject='test-sub'
        )
