import React, { Component } from 'react';
import './RelatedPartsInfo.scss';

class RelatedPartsInfo extends Component {
    render() {
        if (!this.props.parts) {
            return null
        }
        else if (this.props.parts) {
            return (
                <div className="RelatedPartsInfo">
                    <h3 className="process-subtitle">Partes relacionadas</h3>
                    {this.props.parts.map(
                        (part) => (
                            <div key={part.id}>
                                <span>{part.kind}</span>
                                <h3>{part.description}</h3>
                                <div>
                                    {part.related_people.map(
                                        (people) => (
                                            <div key={people.id}>
                                                <span>{people.kind}</span>
                                                <h3>{people.name}</h3>
                                            </div>
                                        )
                                    )}
                                </div>
                            </div>
                        )
                    )}
                </div>
            )
        } else {
            return null;
        }
    }
}

export default RelatedPartsInfo