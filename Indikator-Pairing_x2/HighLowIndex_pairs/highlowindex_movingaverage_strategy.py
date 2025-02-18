import backtrader as bt
from ..base_strategy import FlexibleStrategy

class HighLowIndex_MovingAverage_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von HighLowIndex und MovingAverage
    """
    
    params = (
        ('indicators', {
            'HighLowIndex': {
                'class': HighLowIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HighLowIndex'>
            },
            'MovingAverage': {
                'class': MovingAverage,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MovingAverage'>
            }
        }),
        ('weights', {
            'HighLowIndex': 1.0,
            'MovingAverage': 1.0
        })
    )
