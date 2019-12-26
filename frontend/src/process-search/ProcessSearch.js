import { Input, message } from 'antd';
import React, { Component } from 'react';
import './ProcessSearch.scss';
import axios from 'axios'
import ProcessInfo from './process-info/ProcessInfo'
import qs from 'qs';

const { Search } = Input;

class ProcessSearch extends Component {

    constructor() {
        super();
        this.state = {
            processNumber: null,
            process: null,
            loading: false,
            notFound: false,
        }
    }

    crawlerProcess(processNumber) {
        if(processNumber){
            this.setState({ process: {}, loading: true });
            axios.get(`api/processes/crawler?format=json&process_number=${processNumber}`)
                .then(response => {
                    this.props.history.push(`?processNumber=${processNumber}`);
                    this.setState({ process: response.data, loading: false });
                })
                .catch(response => {
                    this.props.history.push('');
                    this.setState({ process: null, loading: false });
                    message.error('Nenhum processo encontrado com este número');
                })
        } else {
            message.error('Insira o número do processo');
        }
    }

    componentDidMount() {
        let params = qs.parse(this.props.history.location.search, { ignoreQueryPrefix: true });
        if (params.processNumber) {
            this.setState({ processNumber: params.processNumber });
            this.crawlerProcess(params.processNumber);
        }
    }

    handleChange(event) {
        this.setState({ processNumber: event.target.value });
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
                        value={this.state.processNumber}
                        onChange={this.handleChange.bind(this)}
                        onSearch={value => this.crawlerProcess(value)}
                    />
                </div>
                <ProcessInfo process={this.state.process} loading={this.state.loading}/>
            </div>

        )
    }
}

export default ProcessSearch