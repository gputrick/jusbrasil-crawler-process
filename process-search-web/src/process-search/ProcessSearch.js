import { Input } from 'antd';
import React, { Component } from 'react';
import './ProcessSearch.scss';

const { Search } = Input;

class ProcessSearch extends Component {

    crawlerProcess(processNumber){
        console.log(processNumber);
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