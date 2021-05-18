import axiosClient from './axiosClient';

const oj_statusAPI = {
    getAll: () => {
        const url = 'status/';
        return axiosClient.get(url);
    },
    postProblem: (data) =>{
        const token = localStorage.getItem('token');
        let config = {
            headers: {
                'Authorization': 'Token ' + token,
            }
        }
        const url = 'status/';
        return axiosClient.post(url, data, config);
    },
    getById: (id) => {
        const url = `status/${id}`;
        return axiosClient.get(url);
    }
}

export default oj_statusAPI;