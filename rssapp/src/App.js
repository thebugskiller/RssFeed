import React, { useState, useEffect } from 'react';
import Landing from './Pages/Landing';
import { fetchArticles } from './services';

const App = () => {
  const [articles, setArticles] = useState([]);
  const [language, setLanguage] = useState('eng');

  useEffect(() => {
    fetchArticles({ language, setArticles });
  }, [language]);

  return (
    <div>
      <Landing articles={articles} language={language} setLanguage={setLanguage} />
    </div>
  );
};

export default App;
