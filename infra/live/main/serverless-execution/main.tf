provider "aws" {
  region = var.AWS_REGION
}

module "serverless-execution" {
  source = "../../../serverless-execution"

  # aws_account_id = var.AWS_ACCOUNT_ID
}
