import React from 'react';
import ArticleCard from '../components/ArticleCard';
import Header from '../components/Header';
import PropTypes from 'prop-types';

const Landing = ({ articles, language, setLanguage }) => {
  return (
    <>
        <Header language={language} setLanguage={setLanguage} />
        <div className="bg-gray-100 min-h-screen bg-zinc-300 py-8">
        <main className="max-w-7xl mx-auto p-4 bg-white">
            <div className="grid grid-cols-1 gap-4 p-8">
            {articles.length > 0 ? (
                articles.map((article, index) => (
                <ArticleCard key={index} article={article} />
                ))
            ) : (
                <p>No articles available.</p>
            )}
            </div>
        </main>
        </div>
    </>
  );
};

Landing.propTypes = {
    articles: PropTypes.array.isRequired,
    language: PropTypes.string.isRequired,
    setLanguage: PropTypes.func.isRequired,
  };

export default Landing;
