<script setup lang="ts">
const props = defineProps<{ jobDescription: JobDescription }>()

const title = computed(
  () => `[${props.jobDescription.company}] ${props.jobDescription.position} 채용`
)

const position = computed(() => `${props.jobDescription.position} 채용 공고`)

const content = computed(() => {
  const startDate = new Date(props.jobDescription.start_date)
  const endDate = new Date(props.jobDescription.end_date)

  const dateTimeFormte = new Intl.DateTimeFormat('ko-KR', {
    dateStyle: 'full',
    timeZone: 'Australia/Sydney'
  })
  return `합격자에게는 ${props.jobDescription.reward}원의 사이닝 보너스를 드려요.\n
    ${dateTimeFormte.format(startDate)}부터 ${dateTimeFormte.format(endDate)}까지`
})

const skills = computed(() => props.jobDescription.skill.split(',').map((value) => value.trim()))
</script>

<template>
  <article class="job-description-card">
    <h2 class="job-description-card__title">{{ title }}</h2>
    <div>
      <p class="job-description-card__position">{{ position }}</p>
      <div class="job-description-card__skills">
        <span class="job-description-card__skills__item" v-for="skill in skills" :key="skill">
          {{ skill }}
        </span>
      </div>
      <p class="job-description-card__content">{{ content }}</p>
    </div>
  </article>
</template>

<style lang="scss" scoped>
.job-description-card {
  width: fit-content;
  min-width: 240px;
  margin: 8px;
  padding: 18px 24px;
  box-shadow: 2px 2px 4px #dddddd;
  border-radius: 4%;
  &__title {
    font-size: 1.2em;
    font-weight: 600;
    margin: 12px 0;
  }
  &__position {
    font-size: 0.8em;
    font-weight: 600;
    text-align: right;
    margin: 8px 0;
  }
  &__skills {
    display: flex;
    justify-content: flex-end;
    margin: 16px 0;
    &__item {
      font-size: 0.8em;
      font-weight: 600;
      text-align: right;
      padding: 4px 8px;
      background-color: #dddddd;
      box-shadow: 1px 1px 2px #aaaaaa;
      border-radius: 8px;
      &:not(:first-of-type) {
        margin: 0 0 0 6px;
      }
    }
  }
  &__content {
    font-size: 0.8em;
    text-align: right;
    margin: 8px 0;
    white-space: pre-line;
  }
}
</style>
