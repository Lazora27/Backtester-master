import backtrader as bt
from ..base_strategy import FlexibleStrategy

class ArmsEaseOfMovement_EhlersCenterOfGravityOscillator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von ArmsEaseOfMovement und EhlersCenterOfGravityOscillator
    """
    
    params = (
        ('indicators', {
            'ArmsEaseOfMovement': {
                'class': ArmsEaseOfMovement,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ArmsEaseOfMovement'>
            },
            'EhlersCenterOfGravityOscillator': {
                'class': EhlersCenterOfGravityOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_EhlersCenterOfGravityOscillator'>
            }
        }),
        ('weights', {
            'ArmsEaseOfMovement': 1.0,
            'EhlersCenterOfGravityOscillator': 1.0
        })
    )
