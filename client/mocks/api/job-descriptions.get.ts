import type { HttpHandler } from 'msw'
import { http, HttpResponse } from 'msw'

import { data } from './data/job-descriptions.data'

const api: HttpHandler = http.get('http://49.1.213.232:8000/api/v1/job-descriptions', () => {
  return HttpResponse.json(data)
})

export default api
