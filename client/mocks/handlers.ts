import type { HttpHandler } from 'msw'

import getCompanies from './api/companies.get'

export const handlers: HttpHandler[] = [getCompanies]
