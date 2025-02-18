import backtrader as bt
from ..base_strategy import FlexibleStrategy

class TickActivityIndex_HullMovingAverage_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von TickActivityIndex und HullMovingAverage
    """
    
    params = (
        ('indicators', {
            'TickActivityIndex': {
                'class': TickActivityIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TickActivityIndex'>
            },
            'HullMovingAverage': {
                'class': HullMovingAverage,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HullMovingAverage'>
            }
        }),
        ('weights', {
            'TickActivityIndex': 1.0,
            'HullMovingAverage': 1.0
        })
    )
