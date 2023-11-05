<script setup lang="ts">
const props = defineProps<{ jobDescription: JobDescription }>()

const rewardFormat = new Intl.NumberFormat('ko-KR', { currency: 'KRW' })
const dateTimeFormat = new Intl.DateTimeFormat('ko-KR', {
  dateStyle: 'long',
  timeZone: 'Asia/Seoul'
})
const formatDate = (date: Date) => dateTimeFormat.format(date).replace(/\s+/g, '&nbsp;')

const title = computed(
  () => `[${props.jobDescription.company.company_name}] ${props.jobDescription.position} 채용`
)

const position = computed(() => `${props.jobDescription.position} 채용 공고`)

const content = computed(() => {
  const bonus = rewardFormat.format(props.jobDescription.reward)
  return `합격자에게는 ${bonus}원의 사이닝 보너스를 드려요.`
})

const range = computed(() => {
  const start = formatDate(new Date(props.jobDescription.start_date))
  const end = formatDate(new Date(props.jobDescription.end_date))

  return `<strong style="font-weight: 600;">${start}</strong>부터 <strong style="font-weight: 600;">${end}</strong>까지`
})

const skills = computed(() => props.jobDescription.skill.split(',').map((value) => value.trim()))

const region = computed(() => {
  return `${props.jobDescription.company.country} ${props.jobDescription.company.city}`
})
</script>

<template>
  <article class="job-description-card">
    <h2 class="job-description-card__title">{{ title }}</h2>
    <div>
      <p class="job-description-card__position">{{ position }}</p>
      <p class="job-description-card__region">{{ region }}</p>
      <p class="job-description-card__content">{{ content }}</p>
      <p class="job-description-card__range" v-html="range"></p>
      <div class="job-description-card__skills">
        <span class="job-description-card__skills__item" v-for="skill in skills" :key="skill">
          {{ skill }}
        </span>
      </div>
    </div>
  </article>
</template>

<style lang="scss" scoped>
.job-description-card {
  margin: 8px;
  padding: 18px 24px;
  box-shadow: 2px 2px 4px #dddddd;
  border-radius: 4%;
  &__title {
    min-height: 2.4em;
    font-size: 1em;
    font-weight: 600;
    margin: 12px 0;
    word-break: keep-all;
  }
  &__position {
    font-size: 0.8em;
    font-weight: 600;
    text-align: right;
    margin: 8px 0;
  }
  &__region {
    font-size: 0.6em;
    font-weight: 600;
    text-align: right;
    margin: 8px 0;
  }
  &__content {
    margin: 16px 0;
    font-size: 0.8em;
    white-space: pre-line;
    word-break: keep-all;
  }
  &__range {
    margin: 16px 0;
    font-size: 0.8em;
    line-height: 1.2em;
    text-align: right;
    white-space: pre-line;
    word-break: keep-all;
  }
  &__skills {
    display: flex;
    justify-content: flex-end;
    margin: 32px 0;
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
}
</style>
