import { Input } from 'antd';
import React, { Component } from 'react';
import './ProcessSearch.scss';
import axios from 'axios'

const { Search } = Input;

class ProcessSearch extends Component {

    constructor(){
        super();
        this.state = {process: {}}
    }

    crawlerProcess(processNumber){

        axios.get(`/processes/crawler?process_number=${processNumber}`)
        .then( process => { 
            this.setState({process: process})
        })
    }
    
    render() {
        return (
            <div className="ProcessSearch">
                <span className="title">Busca de processos</span>
                <div className="content">
                    <h1>Buscar processo</h1>
                    <Search
                        placeholder="Insira o número do processo"
                        enterButton="Buscar"
                        size="large"
                        onSearch={value => this.crawlerProcess(value)}
                    />
                </div>
            </div>
        )
    }
}

export default ProcessSearch