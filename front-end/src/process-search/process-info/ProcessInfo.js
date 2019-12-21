
import { Skeleton } from 'antd';
import React, { Component } from 'react';
import MovesInfo from '../moves-info/MovesInfo';
import './ProcessInfo.scss';

class ProcessInfo extends Component {
    render() {
        if (this.props.loading) {
            return (<Skeleton active paragraph={{ rows: 1 }} />)
        }
        else if(this.props.process) {
            return (
                <div className="ProcessInfo">
                    <h1> Processo n. {this.props.process.process_number} do TJAL</h1>
                    <span>Distribuido em {this.props.process.distribuition}</span>
                    <MovesInfo moves={this.props.process.moves} />
                </div>
            )
        } else {
            return null;
        }
    }
}

export default ProcessInfo