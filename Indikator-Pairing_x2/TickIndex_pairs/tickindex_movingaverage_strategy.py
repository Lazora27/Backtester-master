import backtrader as bt
from ..base_strategy import FlexibleStrategy

class TickIndex_MovingAverage_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von TickIndex und MovingAverage
    """
    
    params = (
        ('indicators', {
            'TickIndex': {
                'class': TickIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TickIndex'>
            },
            'MovingAverage': {
                'class': MovingAverage,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MovingAverage'>
            }
        }),
        ('weights', {
            'TickIndex': 1.0,
            'MovingAverage': 1.0
        })
    )
