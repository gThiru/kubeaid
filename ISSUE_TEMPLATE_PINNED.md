# 🚀 What is KubeAID?

**KubeAID** is an AI-powered assistant that helps you diagnose, understand, and fix issues in your Kubernetes clusters — fast.

Whether you’re facing a `CrashLoopBackOff`, image pull errors, or failing deployments, KubeAID automates troubleshooting by combining Kubernetes APIs with powerful large language models like GPT.

---

## 🧠 Key Features

- 🤖 **AI-Powered Root Cause Analysis** using GPT
- 📄 Understand `kubectl describe` and logs in plain English
- ⚙️ Auto-remediation suggestions (e.g., restart pods, fix env issues)
- 💬 CLI-based, and **ChatOps-ready** (Slack/Teams integration coming)
- 🔐 Works with your existing kubeconfig / access

---

## 🛠️ How It Works
```bash
kubeaid --namespace default --pod my-app --auto-fix
```

- Connects to your cluster and pulls pod state + logs
- Analyzes the issue with GPT
- Shows a diagnosis and actionable fix suggestions
- Can optionally **auto-restart** unhealthy pods

---

## 🌍 Why It Matters
DevOps and SRE teams lose valuable time on repetitive troubleshooting.

KubeAID gives every engineer a smart assistant that:
- Speaks Kubernetes
- Reads logs
- Suggests fixes
- Saves you hours of guesswork

---

## 🧩 Roadmap
- ✅ v0.1: CLI with AI diagnosis + restart auto-fix
- 🛠️ v0.2: Prometheus/Grafana integration
- 🔗 v0.3: Slack/ChatOps support
- 💬 v0.4: LLM-based drift detection

---

## 📬 Want to Contribute?
- ⭐ Star the repo
- 🍴 Fork and submit PRs
- 🐞 File issues or feature requests

Let's build smarter DevOps tools together!

---

**Built with ❤️ by [Thiru G](https://www.linkedin.com/in/thiru-g) | MIT Licensed**

