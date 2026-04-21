import boto3

def generar_reporte():
    ec2 = boto3.client('ec2')
    s3 = boto3.client('s3')

    with open("reporte_recursos.txt", "w") as f:
        f.write("--- REPORTE AUTOMATIZADO DE RECURSOS ---\n")

        # Listar instancias
        instancias = ec2.describe_instances()
        f.write("\nInstancias detectadas:\n")
        for reservation in instancias['Reservations']:
            for instance in reservation['Instances']:
                f.write(f"- ID: {instance['InstanceId']} | Estado: {instance['State']['Name']}\n")

        # Listar buckets
        buckets = s3.list_buckets()
        f.write("\nBuckets S3 detectados:\n")
        for b in buckets['Buckets']:
            f.write(f"- {b['Name']}\n")

    print("Reporte generado con éxito en reporte_recursos.txt")

if __name__ == "__main__":
    generar_reporte()
