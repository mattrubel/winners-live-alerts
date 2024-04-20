provider "aws" {
  region = var.AWS_REGION
}

module "notifications" {
  source = "../../../notifications"

  aws_account_id = var.AWS_ACCOUNT_ID
}
