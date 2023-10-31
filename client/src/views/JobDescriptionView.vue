<script setup lang="ts">
const { data } = useFetchJobDescriptions()
</script>

<template>
  <main>
    <template v-if="data">
      <JobDescriptionsBoard
        heading="나갈 때는 마음대로였겠지만 들어올 때는 아니란다"
        :job-descriptions="data"
      />
    </template>
  </main>
</template>

<style></style>
