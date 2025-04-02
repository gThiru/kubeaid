# fix_recommender.py
# Optional module to recommend or apply basic auto-remediations

from kubernetes import client, config

def restart_pod(namespace: str, pod_name: str):
    """
    Deletes the pod so it restarts if part of a deployment/replica set
    """
    config.load_kube_config()
    v1 = client.CoreV1Api()
    try:
        response = v1.delete_namespaced_pod(name=pod_name, namespace=namespace)
        return f"✅ Pod '{pod_name}' in namespace '{namespace}' deleted for restart."
    except client.exceptions.ApiException as e:
        return f"❌ Failed to delete pod: {e}"


def recommend_fix(diagnosis_text: str):
    """
    Basic keyword-based mapping from AI diagnosis to actionable suggestion.
    This can evolve into a proper NLP classifier later.
    """
    recommendations = []

    if "CrashLoopBackOff" in diagnosis_text or "restart" in diagnosis_text:
        recommendations.append("Suggest restarting the pod.")

    if "missing environment variable" in diagnosis_text:
        recommendations.append("Check and update ConfigMap or Secret mounting.")

    if "ImagePullBackOff" in diagnosis_text:
        recommendations.append("Verify image name, tag, and private registry credentials.")

    if "OOMKilled" in diagnosis_text:
        recommendations.append("Increase memory limits in the deployment spec.")

    if "liveness probe failed" in diagnosis_text:
        recommendations.append("Review probe path, port, and thresholds.")

    if not recommendations:
        recommendations.append("No obvious fix suggested. Please review the diagnosis manually.")

    return recommendations
