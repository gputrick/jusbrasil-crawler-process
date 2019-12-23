import { List } from 'antd';
import React, { Component } from 'react';
import './MovesInfo.scss';
import moment from 'moment';

class MovesInfo extends Component {
    render() {
        if (!this.props.moves) {
            return null
        }
        else if (this.props.moves) {
            return (
                <div className="MovesInfo">
                    <List
                        size="large"
                        header={<h3 style={{ margin: 0 }}>MOVIMENTAÇÕES</h3>}
                        bordered
                        dataSource={this.props.moves}
                        renderItem={move =>
                            (
                                <List.Item>
                                    <div className="column">
                                        <span>{moment(move.date).format('DD/MM/YYYY')}</span>
                                        <h4>{move.description}</h4>
                                    </div>
                                </List.Item>
                            )
                        }
                    />
                </div>
            )
        } else {
            return null;
        }
    }
}

export default MovesInfo