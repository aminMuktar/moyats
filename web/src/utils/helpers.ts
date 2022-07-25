import router from "../routes/index"
import { store } from "../store"

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


export const getFullName = (name) => {
  return `${name.firstName} ${name.lastName}`
}

export const toggleStatusSlider = (type: string, id: string) => {
  store.commit("setActivateSlider", true);
  store.commit("setActiveSlideWindow", `${type}-status`)
  store.commit("setStatusItemId", id)
}


// decrease color opacity by 40% from hex color
export const getOpacity = (hex: string) => {
  const rgb = hex.match(/^#?([0-9a-f]{2})([0-9a-f]{2})([0-9a-f]{2})$/i);
  if (rgb) {
    const r = parseInt(rgb[1], 16);
    const g = parseInt(rgb[2], 16);
    const b = parseInt(rgb[3], 16);
    return `rgba(${r}, ${g}, ${b}, 0.7)`;
  }
  return "";
}

// return hex color light or dark
export const isDark = (hex: string) => {
  const rgb = hex.match(/^#?([0-9a-f]{2})([0-9a-f]{2})([0-9a-f]{2})$/i);
  if (rgb) {
    const r = parseInt(rgb[1], 16);
    const g = parseInt(rgb[2], 16);
    const b = parseInt(rgb[3], 16);
    const brightness = (r + g + b) / 3;
    return brightness < 128 ? true : false;
  }
  return "";
}