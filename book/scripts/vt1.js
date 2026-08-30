const tasks = [{"key": "vt1", "agent": "worker", "model": "openrouter/z-ai/glm-5.3-flash", "task": "Return this exact JSON: {\"ok\":true,\"msg\":\"verifier-live\"}", "output": "/home/ubuntu/repos/prs_analysis/book/events/outputs/vt1_report.md"}];
const r = await runs.all(tasks);
return r;
