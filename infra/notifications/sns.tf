resource "aws_sns_topic" "winners_alert_topic" {
  name = var.sns_topic_name
}
