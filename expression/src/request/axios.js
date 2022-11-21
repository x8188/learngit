/*
 * @Autor: Sakurag1_LSJ
 * @LastEditors: Sakurag1_LSJ
 */
import axios from 'axios'

export default function request(config) {
    console.log(config);
    const instance = axios.create({
        baseURL: "http://124.220.197.196"
    })


    return instance(config);
}
