import backtrader as bt
from ..base_strategy import FlexibleStrategy

class TickActivityIndex_MovingAverage_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von TickActivityIndex und MovingAverage
    """
    
    params = (
        ('indicators', {
            'TickActivityIndex': {
                'class': TickActivityIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TickActivityIndex'>
            },
            'MovingAverage': {
                'class': MovingAverage,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MovingAverage'>
            }
        }),
        ('weights', {
            'TickActivityIndex': 1.0,
            'MovingAverage': 1.0
        })
    )
