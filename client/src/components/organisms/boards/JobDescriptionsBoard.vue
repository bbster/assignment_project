<script setup lang="ts">
defineProps<{
  heading: string
  jobDescriptions: JobDescription[]
}>()
</script>

<template>
  <section class="job-descriptions-board">
    <h2 class="job-descriptions-board__title">{{ heading }}</h2>
    <div class="job-descriptions-board__contents">
      <ul class="job-descriptions-board__contents__cards">
        <li
          class="job-descriptions-board__contents__cards__item"
          v-for="jobDescription in jobDescriptions"
          :key="jobDescription.id"
        >
          <JobDescriptionCard :job-description="jobDescription" />
        </li>
      </ul>
    </div>
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
    word-break: keep-all;
  }
  &__contents {
    &__cards {
      display: flex;
      flex-wrap: wrap;
      &__item {
        width: 50%;
        @media (min-width: 768px) and (max-width: 991px) {
          width: 50%;
        }
        @media (max-width: 768px) {
          width: 100%;
        }
        &__card {
          width: auto;
        }
      }
    }
  }
}
</style>
