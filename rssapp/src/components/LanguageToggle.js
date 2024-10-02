import React from 'react';
import PropTypes from 'prop-types';

const LanguageToggle = ({ language, setLanguage }) => {
  return (
    <div className="flex space-x-4">
      <button
        className={`text-gray-600 hover:text-blue-500 ${language === 'eng' ? 'font-bold' : ''}`}
        onClick={() => setLanguage('eng')}
      >
        ENG
      </button>
      <p>\</p>
      <button
        className={`text-gray-600 hover:text-blue-500 ${language === 'esp' ? 'font-bold' : ''}`}
        onClick={() => setLanguage('esp')}
      >
        ESP
      </button>
    </div>
  );
};

LanguageToggle.propTypes = {
    language: PropTypes.string.isRequired,
    setLanguage: PropTypes.func.isRequired,
  };

export default LanguageToggle;
