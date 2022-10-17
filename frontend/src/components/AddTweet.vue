<template>
  <form class="flex gap-6" @submit.prevent="submit">
    <input type="text" v-model="tweet"
      class="block flex-1 rounded-md border-gray-300 shadow-sm focus:border-indigo-500 focus:ring-indigo-500 sm:text-sm"
      placeholder="Tweet" />
    <input type="text" v-model="name"
      class="block flex-1 rounded-md border-gray-300 shadow-sm focus:border-indigo-500 focus:ring-indigo-500 sm:text-sm"
      placeholder="Name" />
    <button type="submit"
      class="inline-flex items-center justify-center rounded-md border border-transparent bg-indigo-600 px-4 py-2 font-medium text-white shadow-sm hover:bg-indigo-700 focus:outline-none focus:ring-2 focus:ring-indigo-500 focus:ring-offset-2 text-sm">Save</button>
  </form>
</template>

<script>
export default {
  data() {
    return {
      name: '',
      tweet: ''
    }
  },
  methods: {
    submit() {
      this.$emit('add', {
        tweet: this.tweet,
        name: this.name
      })

      this.tweet = ''
      this.name = ''
    }
  }
}
</script>
