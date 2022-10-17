<template>
  <Table>
    <template #header>
      <TableCell isHead isFirst class="w-1/4">Name</TableCell>
      <TableCell isHead class="w-1/2">Tweet</TableCell>
      <TableCell isHead class="w-1/4">Created At</TableCell>
    </template>
    <template #default>
      <tr v-for="tweet in tweets" :key="tweet.id">
        <TableCell isFirst>{{tweet.name}}</TableCell>
        <TableCell>{{tweet.tweet}}</TableCell>
        <TableCell>{{formatDate(tweet.created_at)}}</TableCell>
      </tr>
    </template>
  </Table>
</template>

<script>
import Table from './Table.vue'
import TableCell from './TableCell.vue'

export default {
  components: {
    Table,
    TableCell
  },
  props: {
    tweets: Array
  },
  methods: {
    formatDate(dateStr) {
      const date = new Date(dateStr)

      return `${date.toLocaleDateString()} ${date.toLocaleTimeString()}`
    }
  }
}

</script>
