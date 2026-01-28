'use strict'

document.addEventListener('DOMContentLoaded', function()  {
    const topicList = document.querySelector('search#topics ul');
    const topics = getTopics();

    populateFilter(topicList, topics);
    truncateTopics(topicList, topics);
});

function filterTopic(filter, topicList, topics) {
    const currentFilter = document.querySelector('button.topic.filterTopic');
    const usrMsg = document.querySelector('#usr-msg--filter');

    if (currentFilter) {
        currentFilter.classList.remove('filterTopic');
        currentFilter.ariaPressed = 'false';
        usrMsg.innerText = "Select a topic to filter articles.";
    }
    const topic = filter.innerText;
    const articles = document.querySelectorAll('article');

    if (!currentFilter || currentFilter.innerText !== topic) {
        filter.classList.add('filterTopic');
        filter.ariaPressed = 'true';
        usrMsg.innerText = "Click current filter to remove it, or select a new filter."

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
        filter.classList.remove('filterTopic');
        filter.ariaPressed = 'false';
        articles.forEach(article => article.classList.remove('hidden'));
    }

    updateTruncMsg(topicList, topics);
}

function populateFilter(topicList, topics) {
    topics.forEach(topicName => {
        topicList.appendChild(makeTopicBtn(topicName));
    });

    function makeTopicBtn(topicName) {
        const topicLi = document.createElement('li');
        const topicBtn = document.createElement('button');
        topicBtn.innerText = topicName;
        topicBtn.classList.add('topic');
        topicBtn.addEventListener('click', function() {
            filterTopic(this, topicList, topics);
        });
        topicBtn.ariaPressed = 'false';
        topicLi.appendChild(topicBtn);
        return topicLi;
    };
};

function truncateTopics(topicList, topics) {
    if (topics.length > 6) {
        topicList.classList.add('truncated');
        updateTruncMsg(topicList, topics);
    }

    const showBtn = document.querySelector('#showBtn');
    showBtn.addEventListener('click', showBtnHandler);

    function showBtnHandler() {
        topicList.classList.toggle('truncated');

        if (topicList.classList.contains('truncated')) {
            this.innerText = "Show all topics";
        } else {
            this.innerText = "Show fewer topics";
        }

        updateTruncMsg(topicList, topics);
    };
};

function updateTruncMsg(topicList, topics) {
    const truncMsg = document.querySelector('#usr-msg--truncated');
    const activeFilter = topicList.querySelector('button[aria-pressed="true"]');
    const slice = activeFilter && topics.indexOf(activeFilter.innerText) > 5 ?
        7 : 6;
   
    if (topicList.classList.contains('truncated')) {
        truncMsg.innerText = `Showing ${slice} of ${topics.length} topics`;
    } else {
        truncMsg.innerText = `Showing ${topics.length} of ${topics.length} topics`;
    }
};

function getTopics() {
     const topics = [
        ...new Set(
            [...document.querySelectorAll('.topic')]
                .map(i  => i.innerText)
        )
    ].sort();

    return topics;
};
