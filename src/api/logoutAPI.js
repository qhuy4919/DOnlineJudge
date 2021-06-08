import axiosClient from './axiosClient';

const logoutAPI = {
    logout: () => {
        const url = 'logout/';
        const token = localStorage.getItem('token');
        let config = {
            headers: {
                'Authorization': 'Token ' + token,
            }
        }
        return axiosClient.get(url,config);
    }
}
export default logoutAPI;
