import axios from "axios";


export const api = axios.create({
    baseURL: "http://127.0.0.1:8000/api/v1/"
});

export const userRegistration = async(formData) => {
    const {email, username, password} = formData
    let response = await api.post("users/signup/", {email: email, username: username, password: password})
    if (response.status === 201) {
        let {token, user} = response.data
        localStorage.setItem("token", token)
        api.defaults.headers.common['Authorization'] = `Token ${token}`
        return user
    }
    alert(response.data)
    return null
}

export const userLogIn = async(formData) => {
    const {identifier, password} = formData
    let response = await api.post("users/login/ ", {identifier: identifier, password: password})
    if (response.status === 200) {
        let {token, user} = response.data
        localStorage.setItem("token", token)
        api.defaults.headers.common['Authorization'] = `Token ${token}`
        return user
    }
    alert(response.data)
    return null
}

export const signOut = async(user) => {
    let response = await api.post("users/logout/")
    if (response.status === 204){
        localStorage.removeItem("token")
        delete api.defaults.headers.common['Authorization']
        return null
    }
    alert("Failure to log out.")
}

export const getInfo = async() => {
    let token = localStorage.getItem('token')
    if (token){
        api.defaults.headers.common['Authorization'] = `Token ${token}`
        let response = await api.get("users/info/")
        if (response.status === 200) {
            return response.data.email
        }
        return null
    }
    else {
        return null
    }
}
