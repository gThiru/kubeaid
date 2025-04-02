# main.py
# Entry point for KubeAID CLI with named arguments and fix recommendations

import argparse
import sys
from kube_agent import get_pod_details
from log_collector import get_pod_logs
from ai_diagnoser import diagnose_issue
from fix_recommender import recommend_fix, restart_pod


def run_diagnosis(namespace: str, pod_name: str, container: str = None, auto_fix: bool = False):
    print(f"🔍 Fetching pod details for: {pod_name} in {namespace}...")
    pod = get_pod_details(namespace, pod_name)

    if isinstance(pod, str):
        print(pod)
        return

    print("📄 Fetching logs...")
    logs = get_pod_logs(namespace, pod_name, container)

    if logs.startswith("Error"):
        print(logs)
        return

    print("🤖 Sending data to AI for diagnosis...")
    diagnosis = diagnose_issue(str(pod), logs)

    print("\n💡 Diagnosis Result:")
    print("-----------------------------")
    print(diagnosis)
    print("-----------------------------")

    print("\n🛠️ Suggested Fixes:")
    suggestions = recommend_fix(diagnosis)
    for fix in suggestions:
        print(f"- {fix}")

    if auto_fix and any("restart" in fix.lower() for fix in suggestions):
        print("\n🔧 Attempting auto-restart of the pod...")
        result = restart_pod(namespace, pod_name)
        print(result)


def show_help():
    print("""
KubeAID - AI-powered Kubernetes Troubleshooting Tool

Usage:
  python main.py --namespace <namespace> --pod <pod-name> [--container <container-name>] [--auto-fix]

Options:
  --namespace     Kubernetes namespace of the pod
  --pod           Name of the pod to diagnose
  --container     Optional container name (if multiple containers in pod)
  --auto-fix      Automatically apply basic fixes (e.g., pod restart)
  -h, --help      Show this help message and exit
    """)


if __name__ == "__main__":
    if len(sys.argv) == 1 or any(arg in sys.argv for arg in ["-h", "--help"]):
        show_help()
        sys.exit()

    parser = argparse.ArgumentParser(description="KubeAID - AI-powered Kubernetes Troubleshooting", add_help=False)
    parser.add_argument("--namespace", required=True, help="Kubernetes namespace")
    parser.add_argument("--pod", required=True, help="Name of the pod to diagnose")
    parser.add_argument("--container", help="Container name (optional)", default=None)
    parser.add_argument("--auto-fix", action="store_true", help="Automatically apply basic fixes like pod restart")

    args = parser.parse_args()
    run_diagnosis(namespace=args.namespace, pod_name=args.pod, container=args.container, auto_fix=args.auto_fix)
