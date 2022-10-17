<template>
  <th v-if="isHead" scope="col" class="py-3.5 pl-4 pr-3 text-left text-sm font-semibold text-gray-900"
    :class="{'sm:pl-6': isFirst}">
    <slot></slot>
  </th>
  <td v-else class="px-3 py-4 text-sm text-gray-500" :class="{'sm:pl-6': isFirst}">
    <slot></slot>
  </td>
</template>

<script>
export default {
  props: {
    isHead: Boolean,
    isFirst: Boolean
  }
}
</script>
