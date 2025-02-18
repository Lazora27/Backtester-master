import backtrader as bt
from ..base_strategy import FlexibleStrategy

class TickIndex_HullMovingAverage_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von TickIndex und HullMovingAverage
    """
    
    params = (
        ('indicators', {
            'TickIndex': {
                'class': TickIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TickIndex'>
            },
            'HullMovingAverage': {
                'class': HullMovingAverage,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HullMovingAverage'>
            }
        }),
        ('weights', {
            'TickIndex': 1.0,
            'HullMovingAverage': 1.0
        })
    )
