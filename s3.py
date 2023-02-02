response = client.put_object(
    Body='filetoupload',
    Bucket='examplebucket',
    Key='objectkey',
)


print(response)