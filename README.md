# Keep n8n Alive

使用 GitHub Actions 定期 ping n8n 的 `/healthz` endpoint，  
避免部署在 Hugging Face（或其他 free tier）的 n8n 因長時間無流量而進入 sleep 狀態。

---

## 功能

- 每天定時自動觸發（預設：台灣時間 00:00）
- 發送 HTTP request 至 n8n health check
- 防止服務休眠
- 支援手動觸發（方便測試）

---

## 使用方式

1. 將 workflow 檔案放入：

