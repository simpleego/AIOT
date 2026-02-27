
<script>
  const apiBase = "http://localhost:8000";

  let result = null;
  let error = "";
  let overlayUrl = "";

  async function detectOnce() {
    error = "";
    try {
      const res = await fetch(`${apiBase}/detect_once`, { method: "POST" });
      if (!res.ok) {
        const t = await res.text();
        throw new Error(`${res.status} ${t}`);
      }
      result = await res.json();

      // 캐시 무력화(같은 URL이라 브라우저가 이미지 캐시할 수 있음)
      overlayUrl = `${apiBase}/detect_once_image.jpg?ts=${Date.now()}`;
    } catch (e) {
      error = String(e);
    }
  }
</script>

<main style="padding:16px; display:grid; gap:12px;">
  <h1>YOLO Detect Once</h1>

  <div style="display:flex; gap:10px; align-items:center;">
    <button on:click={detectOnce}>Detect Once</button>
    {#if error}<span style="color:red;">{error}</span>{/if}
  </div>

  <section style="display:grid; grid-template-columns: 1fr 1fr; gap:12px;">
    <div>
      <h3>Live (optional)</h3>
      <img src={`${apiBase}/video`} alt="live" style="width:100%; border:1px solid #ccc; border-radius:8px;" />
    </div>

    <div>
      <h3>Overlay (last detect)</h3>
      {#if overlayUrl}
        <img src={overlayUrl} alt="overlay" style="width:100%; border:1px solid #ccc; border-radius:8px;" />
      {:else}
        <div style="padding:12px; border:1px dashed #aaa; border-radius:8px;">Detect Once를 누르면 표시됩니다.</div>
      {/if}
    </div>
  </section>

  <section>
    <h3>JSON Result</h3>
    <pre style="white-space:pre-wrap; background:#f7f7f7; padding:12px; border-radius:8px;">
{result ? JSON.stringify(result, null, 2) : "Detect Once를 누르세요."}
    </pre>
  </section>
</main>
