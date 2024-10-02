/* eslint-disable no-undef */
export const fetchArticles = async ({ language, setArticles }) => {
    const apiUrl = process.env.REACT_APP_API_URL;

    try {
        const response = await fetch(`${apiUrl}${language === 'esp' ? 'esp/' : 'en/'}`);
        const data = await response.json();
        setArticles(data || []);
    } catch (error) {
        console.error('Error fetching articles:', error);
    }
};
