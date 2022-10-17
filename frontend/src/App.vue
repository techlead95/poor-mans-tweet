<template>
  <div class="h-screen mx-auto max-w-7xl py-12 px-4 sm:px-6 lg:px-8">
    <AddTweet @add="addTweet" />
    <TweetList :tweets="tweets" />
  </div>
</template>

<script>
import AddTweet from './components/AddTweet.vue'
import TweetList from './components/TweetList.vue'

const TWEETS_URL = 'http://127.0.0.1:8000/tweets/'

export default {
  components: {
    AddTweet,
    TweetList
  },
  data() {
    return {
      tweets: []
    }
  },
  mounted() {
    this.loadTweets()
  },
  methods: {
    async loadTweets() {
      this.tweets = await fetch(TWEETS_URL).then(r => r.json())
    },
    async addTweet(tweet) {
      await fetch(TWEETS_URL, {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json'
        },
        body: JSON.stringify(tweet)
      })

      this.loadTweets()
    }
  },
}
</script>
