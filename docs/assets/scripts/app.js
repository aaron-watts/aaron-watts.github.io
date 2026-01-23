'use strict'

document.addEventListener('DOMContentLoaded', function()  {
    const topicList = document.querySelector('search#topics ul');

    populateFilter(topicList);

    truncateTopics(topicList);
    window.addEventListener('resize', function() {
        truncateTopics(topicList);
    });
});

function truncateTopics(topicList) {
    if (isOverflow(topicList)) {
        topicList.classList.add('collapse');
    } else {
        topicList.classList.remove('collapse');
    }
};

function isOverflow({scrollHeight}) {
    return scrollHeight > (window.innerHeight / 3);
};

function filterTopic() {
    const currentFilter = document.querySelector('button.topic.filterTopic');
    const usrMsg = document.querySelector('search #usr-msg');

    if (currentFilter) {
        currentFilter.classList.remove('filterTopic');
        currentFilter.ariaPressed = 'false';
        usrMsg.innerText = "Select a topic to filter articles.";
    }
    const topic = this.innerText;
    const articles = document.querySelectorAll('article');

    if (!currentFilter || currentFilter.innerText !== topic) {
        this.classList.add('filterTopic');
        this.ariaPressed = 'true';
        usrMsg.innerText = "Click current filter to remove it, or choose a new filter."

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

function populateFilter(topicList) {
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
