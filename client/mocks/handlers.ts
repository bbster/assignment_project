import type { HttpHandler } from 'msw'

import getCompanies from './api/companies.get'
import getJobDescriptions from './api/job-descriptions.get'

export const handlers: HttpHandler[] = [getCompanies, getJobDescriptions]
