
import { Skeleton, Divider } from 'antd';
import React, { Component } from 'react';
import MovesInfo from '../moves-info/MovesInfo';
import RelatedPartsInfo from '../related-parts-info/RelatedPartsInfo';
import './ProcessInfo.scss';
import { Row, Col } from 'antd';

class ProcessInfo extends Component {
    render() {
        if (!this.props.process) {
            return null
        } else if (this.props.loading) {
            return (
                <Skeleton className="ProcessInfo" active paragraph={{ rows: 20 }}/>
            )
        } else {
            return (
                <div className="ProcessInfo">
                    <h1> Processo n. {this.props.process.process_number} do TJAL</h1>
                    <span>Distribuido em {this.props.process.distribuition}</span>
                    <Row>
                        <Col span={17}>
                            <MovesInfo moves={this.props.process.moves} />
                        </Col>
                        <Col span={1}></Col>
                        <Col span={6}>
                            <h3 className="process-subtitle">Detalhes do processo</h3>

                            <div className="process-detail">
                                <p>Classe: {this.props.process.kind}</p>
                                <p>Área: {this.props.process.area}</p>
                                <p>Assunto: {this.props.process.subject}</p>
                                <p>Juíz: {this.props.process.judge}</p>
                                <p>Valor da ação: R${this.props.process.action_value}</p>
                            </div>
                            <Divider />
                            <RelatedPartsInfo parts={this.props.process.related_parts} />
                        </Col>
                    </Row>
                </div>
            )
        }
    }
}

export default ProcessInfo