const useTemplateFormat = () => {
  const timeZone = 'Asia/Seoul'
  const currency = 'KRW'

  const IntlCurrency = new Intl.NumberFormat('ko-KR', { currency })
  const IntlDateTime = new Intl.DateTimeFormat('ko-KR', { timeZone, dateStyle: 'long' })

  const formatDate = (date: Date) => IntlDateTime.format(date).replace(/\s+/g, '&nbsp;')
  const formatReward = (value: number) => IntlCurrency.format(value)

  return { formatDate, formatReward }
}

export default useTemplateFormat
