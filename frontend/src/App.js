import React, { useState } from "react";

function App() {
  const [resume, setResume] = useState("");
  const [jd, setJd] = useState("");
  const [result, setResult] = useState(null);
  const [dark, setDark] = useState(false);

  const analyze = async () => {
    const response = await fetch("http://127.0.0.1:8000/match", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({
        resume_text: resume,
        jd_text: jd
      })
    });
    const data = await response.json();
    setResult(data);
  };

  const toggleDarkMode = () => {
    setDark(!dark);
  };

  return (
    <div className={dark ? "min-h-screen bg-gray-900 text-white p-8" : "min-h-screen bg-gray-100 p-8"}>
      
      <h1 className="text-4xl font-bold text-center mb-8">
        AI Resume Job Matcher
      </h1>

      <div className={dark ? "max-w-4xl mx-auto bg-gray-800 p-6 rounded-lg shadow" : "max-w-4xl mx-auto bg-white p-6 rounded-lg shadow"}>

        <textarea
          placeholder="Paste Resume Text"
          className="w-full p-3 border rounded mb-4 text-black"
          rows="5"
          onChange={(e) => setResume(e.target.value)}
        />

        <textarea
          placeholder="Paste Job Description"
          className="w-full p-3 border rounded mb-4 text-black"
          rows="5"
          onChange={(e) => setJd(e.target.value)}
        />

        {/* BUTTONS */}
        <div className="flex flex-wrap justify-center gap-3 my-6">

          <button
            onClick={analyze}
            className="bg-green-600 hover:bg-green-700 text-white px-4 py-2 rounded-lg font-semibold shadow"
          >
            Analyze Match
          </button>

          <button
            className="bg-blue-600 hover:bg-blue-700 text-white px-4 py-2 rounded-lg font-semibold shadow"
          >
            ATS Readability Check
          </button>

          <button
            className="bg-purple-600 hover:bg-purple-700 text-white px-4 py-2 rounded-lg font-semibold shadow"
          >
            Generate Resume Bullet (AI)
          </button>

          <button
            className="bg-orange-600 hover:bg-orange-700 text-white px-4 py-2 rounded-lg font-semibold shadow"
          >
            Download Report
          </button>

          <button
            onClick={toggleDarkMode}
            className="bg-gray-800 hover:bg-black text-white px-4 py-2 rounded-lg font-semibold shadow"
          >
            Toggle Dark Mode
          </button>

        </div>

        {/* RESULT */}
        {result && (
          <div className="mt-6">
            <p className="text-xl font-semibold">
              Match Score: {result.match_score}%
            </p>

            <p className="mt-2 text-green-400">
              ✅ Matched Skills: {result.matched_skills.join(", ")}
            </p>

            <p className="mt-2 text-red-400">
              ❌ Missing Skills: {result.missing_skills.join(", ")}
            </p>
          </div>
        )}
      </div>
    </div>
  );
}

export default App;
