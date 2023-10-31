<script setup lang="ts">
const props = defineProps<{ jobDescription: JobDescription }>()

const title = computed(
  () => `[${props.jobDescription.company}] ${props.jobDescription.position} 채용`
)

const content = computed(
  () =>
    `${props.jobDescription.content}\n합격자에게는 ${props.jobDescription.reward}원의 사이닝 보너스와 함께`
)
</script>

<template>
  <article class="job-description-card">
    <h2 class="job-description-card__title">{{ title }}</h2>
    <div>
      <p class="job-description-card__content">{{ content }}</p>
    </div>
  </article>
</template>

<style lang="scss" scoped>
.job-description-card {
  width: 240px;
  margin: 8px;
  padding: 18px 24px;
  box-shadow: 2px 2px 4px #dddddd;
  border-radius: 4%;
  &__title {
    font-size: 1.2em;
    font-weight: 600;
    margin: 12px 0;
  }
  &__addr {
    font-size: 0.8em;
    text-align: right;
    margin: 8px 0;
  }
}
</style>
