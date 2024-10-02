import React from 'react';
import { formatDate } from '../utils';
import PropTypes from 'prop-types';

const ArticleCard = ({ article }) => {
  const { title, description, image_url, link, pub_date, creator } = article;

  return (
    <div className="p-4 w-full flex flex-col md:flex-row border-b border-gray-200">
      <div className="flex-1 w-full md:w-3/4 pr-4">
        <p className='text-sm'>{formatDate(pub_date)}</p>
        <h2 className="text-xl font-semibold mb-2 hover:text-blue-500 cursor-pointer" onClick={() => window.open(link, "_blank")}>
          {title}
        </h2>
        <p className="text-gray-900">{description}</p>
        <p className="mt-10 text-gray-500">By {creator}</p>
      </div>
      <img className="w-full h-48 object-cover md:w-1/4" src={image_url} alt={title} />
    </div>
  );
};

ArticleCard.propTypes = {
    article: PropTypes.shape({
      title: PropTypes.string.isRequired,
      description: PropTypes.string.isRequired,
      image_url: PropTypes.string.isRequired,
      link: PropTypes.string.isRequired,
      pub_date: PropTypes.string.isRequired,
      creator: PropTypes.string.isRequired,
    }).isRequired,
  };

export default ArticleCard;
