import type { HttpHandler } from 'msw'
import { http, HttpResponse } from 'msw'

const api: HttpHandler = http.get('https://rest-endpoint.example/api/companies', () => {
  return HttpResponse.json([] as Company[])
})

export default api
