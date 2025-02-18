import backtrader as bt
from ..base_strategy import FlexibleStrategy

class PutCallRatio_HullMovingAverage_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von PutCallRatio und HullMovingAverage
    """
    
    params = (
        ('indicators', {
            'PutCallRatio': {
                'class': PutCallRatio,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PutCallRatio1'>
            },
            'HullMovingAverage': {
                'class': HullMovingAverage,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HullMovingAverage'>
            }
        }),
        ('weights', {
            'PutCallRatio': 1.0,
            'HullMovingAverage': 1.0
        })
    )
