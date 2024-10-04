import React from 'react';
import LanguageToggle from './LanguageToggle';
import PropTypes from 'prop-types';

const Header = ({ language, setLanguage }) => {
  const currentDate = new Date().toLocaleDateString('en-US', {
    year: 'numeric',
    month: 'long',
    day: 'numeric',
  });

  return (
    <header className="shadow bg-zinc-300 sticky top-0 z-50">
      <div className="max-w-7xl mx-auto px-4 py-4 flex justify-between items-center">
        <p className="text-lg">{currentDate}</p>
        <h1 className="text-2xl font-bold">The New York Times</h1>
        <LanguageToggle language={language} setLanguage={setLanguage} />
      </div>
    </header>
  );
};

Header.propTypes = {
    language: PropTypes.string.isRequired,
    setLanguage: PropTypes.func.isRequired,
  };

export default Header;
