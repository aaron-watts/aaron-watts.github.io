const populateTopics = () => {
    const isOverflow = ({clientHeight, scrollHeight}) => {
        return scrollHeight > clientHeight;
    };

    const makeTopicTag = (topicName) => {
        const topic = document.createElement('li');
        topic.classList.add('topic');
        topic.innerText = topicName;
        topic.addEventListener('click', filterByTopic);
        return topic;
    };

    const makeButton = () => {
        const showBtn = document.createElement('button');
        showBtn.innerText = 'Show more topics';
        showBtn.classList.add('hidden');
        showBtn.addEventListener('click', () => {
            topicList.classList.toggle('fade');
            topicList.classList.toggle('topic-truncate');
            showBtn.innerText == 'Show more topics' ? 
            showBtn.innerText = 'Show less topics' : 
            showBtn.innerText = 'Show more topics';
        });
        return showBtn;
    }

    const topicContainer = document.querySelector('#topic-list--container');
    const topicList = document.querySelector('#topic-list');
    const topics = [
        ...new Set(
            [...document.querySelectorAll('.topic')]
                .map(i => i.innerText)
        )
    ].sort();

    topics.forEach(topicName => {
        topicList.appendChild(makeTopicTag(topicName));
    });

    const showBtn = makeButton();
    topicContainer.appendChild(showBtn);

    window.addEventListener('resize', function() {
        if (isOverflow(topicList) || topicList.clientHeight > window.innerHeight * .2) {
            showBtn.classList.remove('hidden');
            topicList.classList.add('fade');
        } else {
            showBtn.classList.add('hidden');
            topicList.classList.remove('fade');
        }
    }, true)

    if (isOverflow(topicList)) {
        showBtn.classList.remove('hidden');
        topicList.classList.add('fade');
    } else {
        topicList.classList.remove('fade');
    } 
};

function filterByTopic() {
    const selected = document.querySelector('#topic-list > .topic.selected');
    if (selected) selected.classList.remove('selected');
    const selection = this.innerText;
    const articles = document.querySelectorAll('article');

    if (!selected || selected.innerText !== selection) {
        this.classList.add('selected');

        articles.forEach(article => {
            article.classList.add('hidden');

            const topics = [...article.children[2].children];
            for (let topic of topics) {
                if (topic.innerText.trim() === selection.trim()) {
                    article.classList.remove('hidden');
                }
            }
        });
    } else {
        this.classList.remove('selected');

        articles.forEach(article => article.classList.remove('hidden'));
    }

};

document.addEventListener('DOMContentLoaded', populateTopics);
