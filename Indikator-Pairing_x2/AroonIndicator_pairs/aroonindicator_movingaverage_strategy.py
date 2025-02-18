import backtrader as bt
from ..base_strategy import FlexibleStrategy

class AroonIndicator_MovingAverage_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von AroonIndicator und MovingAverage
    """
    
    params = (
        ('indicators', {
            'AroonIndicator': {
                'class': AroonIndicator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AroonIndicator'>
            },
            'MovingAverage': {
                'class': MovingAverage,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MovingAverage'>
            }
        }),
        ('weights', {
            'AroonIndicator': 1.0,
            'MovingAverage': 1.0
        })
    )
