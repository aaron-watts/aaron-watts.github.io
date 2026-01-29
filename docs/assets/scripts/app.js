'use strict'

document.addEventListener('DOMContentLoaded', function()  {
    document.querySelector('search#topics').classList.remove('noscript');

    const topicList = document.querySelector('search#topics ul');
    const topics = getTopics();
    const truncIndex = parseInt(getTruncIndex());

    populateFilter(topicList, topics, truncIndex);
    truncateTopics(topicList, topics, truncIndex);
});

function populateFilter(topicList, topics, truncIndex) {
    topics.forEach(topicName => {
        topicList.appendChild(makeTopicBtn(topicName));
    });

    function makeTopicBtn(topicName) {
        const topicLi = document.createElement('li');
        const topicBtn = document.createElement('button');
        topicBtn.innerText = topicName;
        topicBtn.classList.add('topic');
        topicBtn.addEventListener('click', function() {
            filterTopic(this, topicList, topics, truncIndex);
        });
        topicBtn.ariaPressed = 'false';
        topicLi.appendChild(topicBtn);
        return topicLi;
    };
};

function filterTopic(filter, topicList, topics, truncIndex) {
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

    updateTruncMsg(topicList, topics, truncIndex);
}

function truncateTopics(topicList, topics, truncIndex) {
    if (topics.length > truncIndex - 1) {
        topicList.classList.add('truncated');
        updateTruncMsg(topicList, topics, truncIndex);
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

        updateTruncMsg(topicList, topics, truncIndex);
    };
};

function updateTruncMsg(topicList, topics, truncIndex) {
    const truncMsg = document.querySelector('#usr-msg--truncated');
    const activeFilter = topicList.querySelector('button[aria-pressed="true"]');
    const slice = activeFilter && topics.indexOf(activeFilter.innerText) > truncIndex - 2 ?
        truncIndex : truncIndex - 1;
   
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

function getTruncIndex() {
    const rules = document.styleSheets[0].cssRules;

    for (let rule of rules) {
        if (rule.selectorText == 'search#topics') {
            return getNumberAfterSubstring('nth-of-type', rule.cssText);
        }
    }
};

function getNumberAfterSubstring(substring, text) {
    let re = new RegExp(substring + '.*?(\\d\)'), match = re.exec(text);
    if (match === null) {
        return '';
    }
    return match[1];
}
