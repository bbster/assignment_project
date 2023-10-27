import { z } from 'zod'

const CompanyId = z.number().optional()

const Company = z.object({
  id: CompanyId,
  company_name: z.string().max(100),
  country: z.string(),
  city: z.string()
})
