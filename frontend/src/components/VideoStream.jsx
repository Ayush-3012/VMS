import { useState, useEffect } from "react";
import { getResults } from "../services/api";

function VideoStream() {
  const [results, setResults] = useState({});

  useEffect(() => {
    const fetchResults = async () => {
      const data = await getResults();
      setResults(data);
    };

    fetchResults();
    const interval = setInterval(fetchResults, 2000);

    return () => clearInterval(interval);
  }, []);

  return (
    <div style={{ padding: "20px" }}>
      <div
        style={{
          display: "grid",
          gridTemplateColumns: "repeat(auto-fill, minmax(320px, 1fr))",
          gap: "20px",
        }}
      >
        {Object.keys(results).map((video) => (
          <div
            key={video}
            style={{
              border: "1px solid #ccc",
              borderRadius: "8px",
              padding: "10px",
              backgroundColor: "#f9f9f9",
              boxShadow: "0 2px 5px rgba(0,0,0,0.1)",
            }}
          >
            <h3 style={{ marginBottom: "10px" }}>{video}</h3>
            <video
              src={`/videos/${video}`}
              width="100%"
              height="auto"
              autoPlay
              muted
              controls
              style={{ borderRadius: "5px", marginBottom: "10px" }}
            />

            <div
              style={{
                maxHeight: "200px",
                overflowY: "auto",
                backgroundColor: "#fff",
                padding: "5px",
                borderRadius: "5px",
                border: "1px solid #ddd",
              }}
            >
              {results[video].map((frameData, idx) => (
                <div
                  key={idx}
                  style={{
                    margin: "2px 0",
                    fontSize: "14px",
                    display: "flex",
                    justifyContent: "space-between",
                    alignItems: "center",
                  }}
                >
                  <span>
                    Frame {frameData.frame}: {frameData.faces} faces,{" "}
                    {frameData.persons} persons
                  </span>
                  {frameData.alerts && frameData.alerts.length > 0 && (
                    <span style={{ color: "red", fontWeight: "bold" }}>
                      {frameData.alerts.join(", ")}
                    </span>
                  )}
                </div>
              ))}
            </div>
          </div>
        ))}
      </div>
    </div>
  );
}

export default VideoStream;
