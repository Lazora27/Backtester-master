import backtrader as bt
from ..base_strategy import FlexibleStrategy

class AroonIndicator_SimpleMovingAverage_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von AroonIndicator und SimpleMovingAverage
    """
    
    params = (
        ('indicators', {
            'AroonIndicator': {
                'class': AroonIndicator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AroonIndicator'>
            },
            'SimpleMovingAverage': {
                'class': SimpleMovingAverage,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SimpleMovingAverage'>
            }
        }),
        ('weights', {
            'AroonIndicator': 1.0,
            'SimpleMovingAverage': 1.0
        })
    )
