import { z } from 'zod'

const companyId = z.number()

export const company = z.object({
  id: companyId,
  company_name: z.string().max(100),
  country: z.string(),
  city: z.string()
})
