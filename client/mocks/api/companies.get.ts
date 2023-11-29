import type { HttpHandler } from 'msw'
import { http, HttpResponse } from 'msw'

import { data } from './data/companies.data'

const api: HttpHandler = http.get('http://49.1.213.232:8000/api/v1/companies', () => {
  return HttpResponse.json(data)
})

export default api
