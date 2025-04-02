from kubernetes import client, config

def get_pod_logs(namespace: str, pod_name: str, container: str = None):
    config.load_kube_config()
    v1 = client.CoreV1Api()
    try:
        logs = v1.read_namespaced_pod_log(name=pod_name, namespace=namespace, container=container)
        return logs
    except client.exceptions.ApiException as e:
        return f"Error fetching pod logs: {e}"