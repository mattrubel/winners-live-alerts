module "lambda" {
  source = "terraform-aws-modules/lambda/aws"

  function_name = "serverless-execution-function"
  description   = "Serverless Execution Function"
  handler       = "src.handler.event_handler"
  runtime       = "python3.11"

  timeout = 60

  lambda_role = aws_iam_role.serverless_execution_role.arn

  source_path = "../../../../function/."

}