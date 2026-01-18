'use strict'

function filterTopic() {
    const currentFilter = document.querySelector('button.topic.filterTopic');
    if (currentFilter) {
        currentFilter.classList.remove('filterTopic');
        currentFilter.ariaPressed = 'false';
    }
    const topic = this.innerText;
    const articles = document.querySelectorAll('article');

    if (!currentFilter || currentFilter.innerText !== topic) {
        this.classList.add('filterTopic');
        this.ariaPressed = 'true';

        articles.forEach(article => {
            article.classList.add('hidden');

            const articleTopics = [...article.querySelectorAll('.topic')];
            for (let articleTopic of articleTopics) {
                if (articleTopic.innerText.trim() === topic.trim()) {
                    article.classList.remove('hidden');
                }
            }
        });
    } else {
        this.classList.remove('filterTopic');
        this.ariaPressed = 'false';
        articles.forEach(article => article.classList.remove('hidden'));
    }

}

function populateFilter() {
    const topicContainer = document.querySelector('#topic-list--container');
    const topicList = document.querySelector('#topic-list');

    const topics = [
        ...new Set(
            [...document.querySelectorAll('.topic')]
                .map(i  => i.innerText)
        )
    ].sort();

    topics.forEach(topicName => {
        topicList.appendChild(makeTopicBtn(topicName));
    });

    function makeTopicBtn(topicName) {
        const topicLi = document.createElement('li');
        const topicBtn = document.createElement('button');
        topicBtn.innerText = topicName;
        topicBtn.classList.add('topic');
        topicBtn.addEventListener('click', filterTopic);
        topicBtn.ariaPressed = 'false';
        topicLi.appendChild(topicBtn);
        return topicLi;
    };
}

document.addEventListener('DOMContentLoaded', populateFilter);
