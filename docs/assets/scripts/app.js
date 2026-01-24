'use strict'

document.addEventListener('DOMContentLoaded', function()  {
    const topicList = document.querySelector('search#topics ul');
    const topics = getTopics();

    populateFilter(topicList, topics);
    truncateTopics(topicList, topics);
});


function filterTopic() {
    const currentFilter = document.querySelector('button.topic.filterTopic');
    const usrMsg = document.querySelector('#usr-msg #filter');

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
        this.classList.remove('filterTopic');
        this.ariaPressed = 'false';
        articles.forEach(article => article.classList.remove('hidden'));
    }

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
        topicBtn.addEventListener('click', filterTopic);
        topicBtn.ariaPressed = 'false';
        topicLi.appendChild(topicBtn);
        return topicLi;
    };
};

function truncateTopics(topicList, topics) {
    const truncMsg = document.querySelector('#usr-msg #truncated');

    if (topics.length > 6) {
        topicList.classList.add('truncated');
        truncMsg.innerText = `(Showing 6 of ${topics.length} topics)`;
        makeShowBtn();
    }

    function makeShowBtn() {
        const btnContainer = document.querySelector('#showBtn--container');
        const showBtn = document.createElement('button');
        showBtn.innerText = "Show all topics"
        showBtn.addEventListener('click', showBtnHandler);
        btnContainer.appendChild(showBtn);
    };

    function showBtnHandler() {
        topicList.classList.toggle('truncated');

        if (topicList.classList.contains('truncated')) {
            this.innerText = "Show all topics";
            truncMsg.innerText = `(Showing 6 of ${topics.length} topics)`
        } else {
            this.innerText = "Show fewer topics";
            truncMsg.innerText = `(Showing ${topics.length} of ${topics.length} topics)`
        }
    };
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
