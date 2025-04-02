# KubeAID

**AI-Powered Kubernetes Diagnosis Assistant**

KubeAID is an intelligent assistant designed to diagnose and explain issues in your Kubernetes cluster using AI. It integrates with your cluster to fetch pod data, logs, and configurations, then leverages large language models (LLMs) like GPT to provide root cause analysis and actionable suggestions.

## 🔍 What It Does

- Analyzes crashing pods and failed deployments
- Fetches real-time logs and cluster state
- Uses LLMs to summarize root causes and suggest fixes
- CLI and future ChatOps interface (Slack support planned)
- Optional: auto-remediation and rollback support

## 📁 Project Structure

```
kubeaid/
├── kube_agent.py           # K8s pod/deployment info fetcher
├── log_collector.py        # Logs from failing pods
├── ai_diagnoser.py         # GPT-based diagnosis logic
├── fix_recommender.py      # Suggest/perform automated fixes (optional)
├── chatops_interface.py    # Slack/ChatGPT interface (planned)
├── main.py                 # CLI interface
├── .env.example            # Env file for secrets (OpenAI key, etc.)
├── requirements.txt        # Python dependencies
├── .gitignore              # Standard Python exclusions
├── README.md               # This file
└── LICENSE                 # MIT License
```

## 🧠 Use Cases
- Troubleshooting `CrashLoopBackOff` pods
- Diagnosing image pull issues, DNS failures, or missing env vars
- Getting human-readable summaries of `kubectl describe` outputs
- Helping L1/L2 engineers with root cause suggestions

## 🛠️ Setup

1. Clone the repo:
```bash
git clone https://github.com/yourusername/kubeaid.git
cd kubeaid
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Create a `.env` file:
```bash
cp .env.example .env
# Add your OpenAI API Key
```

4. Run the CLI:
```bash
python main.py --namespace default --pod my-app --auto-fix
```
## 🆘 Show Help

**KubeAID - AI-powered Kubernetes Troubleshooting Tool**

### 📌 Usage:
```bash
python main.py --namespace <namespace> --pod <pod-name> [--container <container-name>] [--auto-fix]
```
### ⚙️ Options

| Option            | Description                                                       |
|-------------------|-------------------------------------------------------------------|
| `--namespace`     | Kubernetes namespace of the pod                                   |
| `--pod`           | Name of the pod to diagnose                                       |
| `--container`     | (Optional) Container name (if multiple containers in the pod)     |
| `--auto-fix`      | Automatically apply basic fixes (e.g., pod restart)               |
| `-h`, `--help`    | Show this help message and exit                                   |

## 🔐 Environment Variables
```
OPENAI_API_KEY=your_openai_api_key_here
```

## 🔧 To Install Locally and Run as kubeaid
```
pip install .
kubeaid --namespace default --pod my-app
```

## 📌 Requirements
- Python 3.8+
- Access to a K8s cluster (via `kubectl` or kubeconfig)
- OpenAI API Key (or any LLM provider)

## 🧩 Coming Soon
- ChatOps interface (Slack, Teams)
- Auto-remediation modules
- Integration with Prometheus/Grafana logs

## 📄 License
This project is licensed under the [MIT License](LICENSE).

---

Built with ❤️ to make DevOps smarter, faster, and AI-powered.

