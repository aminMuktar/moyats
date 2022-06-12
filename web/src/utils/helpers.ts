import router from "../routes/index"

export const parseDate = (timestamp: string) => {
  return new Date(timestamp).toLocaleString()
}

export const formAddress = (addr: any) => {
  return `${addr.city}, ${addr.country}`
}

export const formFullName = (first: string, last: string) => {
  return `${first} ${last}`
}
export const updateQparams = (path: string, page: number, pageSize: number) => {
  router.push({
    path: path,
    query: { page: page, pageSize: pageSize },
  })
}

export const formatContacts = (contacts: any) => {
  return contacts.map((e: any) => `${e.firstName}, ${e.email}<br/>`).join("\n");
}
