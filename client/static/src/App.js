// Import thu vien
import React from "react";
//import ReactDom from 'react-dom';
import InputNumber from 'react-input-number';
import axiosBase from 'axios';

const apiUrl = {
    boitoan:"/boitoan/",
};

const axios = axiosBase.create({
    baseURL: "http://127.0.0.1:5000"
});

class App extends React.Component {
    constructor(props) {
        // props thuoc tinh
        super(props);
        // gia tri luu o trong component
        this.state = {
            value: '',
            manYear: 2000,
            womanYear: 2000,
            result: ''
        };

        this.manYearChangeHandler = this.manYearChangeHandler.bind(this);
        this.womanYearChangeHandler = this.womanYearChangeHandler.bind(this);
        this.onClickXemNguHanh = this.onClickXemNguHanh.bind(this);
    }

    manYearChangeHandler = (Year) => {
        this.setState({manYear: Year});
    }

    womanYearChangeHandler = (Year) => {
        this.setState({womanYear: Year});
    }

    // khong dong bo
    onClickXemNguHanh = async() => {
        try{
            
            let obj = {'man_menh': this.state.manYear, 'woman_menh': this.state.womanYear, 'ngu_hanh':''}
            let response = await axios.post(apiUrl.boitoan, obj);
            console.log(response)
            console.log(typeof(response))
//            this.setState({result: response.data.toString()})
            this.setState({result: JSON.stringify(response.data)})
            return response;
        } catch (error) {
            // Handle error
            return error.response;
        }
    }

    onClickXemHopTuoi = async() => {
        try{
            
            let obj = {'man_menh': this.state.manYear, 'woman_menh': this.state.womanYear, 'hop_tuoi':''}
            let response = await axios.post(apiUrl.boitoan, obj);
            console.log(response)
            console.log(typeof(response))
//            this.setState({result: response.data.toString()})
            this.setState({result: JSON.stringify(response.data)})
            return response;
        } catch (error) {
            // Handle error
            return error.response;
        }
    }

    render() {
        return (
            <div>
                <div style={{backgroundColor:'Violet', fontSize:'50px', textAlign:'center'}}>
                    XEM NGŨ HÀNH VÀ HỢP TUỔI.
                </div>

                <div style={{backgroundColor:'Orange', fontSize:'30px', textAlign:'center'}}>
                    Nhập năm sinh âm lịch của bạn Trai và bạn Gái bên dưới.
                </div>

                <div>
                    <label>Năm sinh bạn Nam:</label>
                    <InputNumber min={1950} max={2021} step={1} value={this.state.manYear} onChange={this.manYearChangeHandler}/>
                </div>

                <div>
                    <label>Năm sinh bạn Nữ:</label>
                    <InputNumber min={1950} max={2030} step={1} value={this.state.womanYear} onChange={this.womanYearChangeHandler}/>
                </div>

                <button variant="primary" onClick={this.onClickXemNguHanh}>Xem Ngũ hành</button>{' '}
                <button variant="primary" onClick={this.onClickXemHopTuoi}>Xem Hợp tuổi</button>{' '}

                <div>
                    {this.state.result}
                </div>

            </div>
        );
    }
}

export default App;
