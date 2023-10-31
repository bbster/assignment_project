<script setup lang="ts">
defineProps<{
  heading: string
  jobDescriptions: JobDescription[]
}>()
</script>

<template>
  <section class="job-descriptions-board">
    <h2 class="job-descriptions-board__title">{{ heading }}</h2>
    <ul>
      <li>
        <JobDescriptionCard
          v-for="jobDescription in jobDescriptions"
          :job-description="jobDescription"
          :key="jobDescription.id"
        ></JobDescriptionCard>
      </li>
    </ul>
  </section>
</template>

<style lang="scss" scoped>
.job-descriptions-board {
  margin: 12px 18px;
  padding: 18px 24px;
  &__title {
    margin: 18px;
    font-size: 1.6rem;
    font-weight: 600;
  }
}
</style>
