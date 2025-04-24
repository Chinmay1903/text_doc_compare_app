import React, { useState } from 'react';
import axios from 'axios';

function MultipleFileUpload() {
  const [files, setFiles] = useState([]);
  const [result, setResult] = useState(null);

  const handleUpload = async () => {
    const formData = new FormData();
    for (let file of files) formData.append("files", file);

    try {
      const res = await axios.post("http://localhost:8000/api/compare/", formData);
      setResult(res.data);
    } catch (err) {
      console.error(err);
    }
  };

  const renderResults = () => {
    if (!result) return null;
    return (
      <table border="1">
        <thead>
          <tr>
            <th> File Pair </th>
            <th> Similarity Score </th>
          </tr>
        </thead>
        <tbody>
          {result.results.map((r, i) => (
            <tr key={i}>
              <td> {r.pair} </td>
              <td> {r.score} </td>
            </tr>
          ))}
        </tbody>
      </table>
    );
  };  

  return (
    <div>
      <h2>Upload Multiple Text Files</h2>
      <input type="file" multiple accept=".txt,.pdf" onChange={(e) => setFiles([...e.target.files])} />
      <button onClick={handleUpload}>Compare</button>
      {renderResults()}
    </div>
  );
}

export default MultipleFileUpload;
