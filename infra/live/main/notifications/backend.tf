terraform {
  backend "s3" {
    bucket         = "terraform-597426459950"
    key            = "winners-live-alerts/notifications/terraform.tfstate"
    region         = "us-east-1"
    dynamodb_table = "tf-state-lock"
  }
}
