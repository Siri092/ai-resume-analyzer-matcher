// script.js

async function analyzeMatch() {
  const resume = document.getElementById("resume").value.trim();
  const jd = document.getElementById("jd").value.trim();

  if (!resume || !jd) {
    document.getElementById("result").textContent = "Please enter both Resume and Job Description.";
    return;
  }

  try {
    const response = await fetch("http://127.0.0.1:8000/match", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ resume_text: resume, jd_text: jd })
    });

    if (!response.ok) {
      throw new Error(`Server error: ${response.status}`);
    }

    const data = await response.json();
    document.getElementById("result").textContent = JSON.stringify(data, null, 2);
  } catch (err) {
    document.getElementById("result").textContent = `Error: ${err.message}`;
  }
}

async function analyzeGap() {
  const resume = document.getElementById("resume").value.trim();
  const jd = document.getElementById("jd").value.trim();

  if (!resume || !jd) {
    document.getElementById("result").textContent = "Please enter both Resume and Job Description.";
    return;
  }

  try {
    const response = await fetch("http://127.0.0.1:8000/gap", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ resume_text: resume, jd_text: jd })
    });

    if (!response.ok) {
      throw new Error(`Server error: ${response.status}`);
    }

    const data = await response.json();
    document.getElementById("result").textContent = JSON.stringify(data, null, 2);
  } catch (err) {
    document.getElementById("result").textContent = `Error: ${err.message}`;
  }
}

// Optional: Bind buttons if using onclick in HTML
document.getElementById("matchBtn")?.addEventListener("click", analyzeMatch);
document.getElementById("gapBtn")?.addEventListener("click", analyzeGap);
