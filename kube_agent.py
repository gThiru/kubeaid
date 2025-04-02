from kubernetes import client, config

def get_pod_details(namespace: str, pod_name: str):
    config.load_kube_config()
    v1 = client.CoreV1Api()
    try:
        pod = v1.read_namespaced_pod(name=pod_name, namespace=namespace)
        return pod
    except client.exceptions.ApiException as e:
        return f"Error fetching pod details: {e}"