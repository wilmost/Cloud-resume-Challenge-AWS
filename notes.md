

# Route 53 record

```yml
MyRoute53Record:
    Type: "AWS::Route53::RecordSetGroup"
    Properties: 
        HostedZoneId: Z02249571L3EN5RTX0NIM
        RecordSets:
            - Name: wilmomartinez.com
              Type: A
              AliasTarget:
                HostedZoneId: Z2FDTNDATAQYW2 # cloudfront
                DNSName: !Getatt MyDistribution.DomainName
``` 



```yml
Mycertificate:
    Type: AWS::CertificateManager::Certificate
    Properties: 
        DomainName: wilmomartinez.com
        ValidationMethod: DNS

    
#MyDistribution:
    #Properties:
        ViewerCertificate:
            AcmCertificateArn: !Ref Mycertificate
            SslSupportMethod: sni-only

```


9. Setup-JS

```js

fetch   


```
10.

```yml

DynamoDBTable: 
    Type: AWS::DynamoDB::Table
    Properties:
        TableName: cloud-resume-challenge
        BillingMode: PAY_PER_REQUEST
        AttributeDefinitions: 
            - AttributeName: "ID"
            - AttributeType: "S"
        KeySchema:
            - AttributeName: "ID"
              keyType: "HASH"



```
