# aws-dynamodb-streams-to-lambda

 - DDB object used for tets:
```
{
  "date": "Dec 30 2020 17:40:00",
  "deviceId": "D150",
  "name": "jgilson"
}
```

 - IAM permission required:
```
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Effect": "Allow",
            "Action": [
                "dynamodb:DescribeStream",
                "dynamodb:GetRecords",
                "dynamodb:GetShardIterator",
                "dynamodb:ListStreams",
                "logs:CreateLogGroup",
                "logs:CreateLogStream",
                "logs:PutLogEvents"
            ],
            "Resource": "*"
        }
    ]
}
```