import backtrader as bt
from ..base_strategy import FlexibleStrategy

class DOMDepth_ExponentialMovingAverage_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von DOMDepth und ExponentialMovingAverage
    """
    
    params = (
        ('indicators', {
            'DOMDepth': {
                'class': DOMDepth,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_DOMDepth'>
            },
            'ExponentialMovingAverage': {
                'class': ExponentialMovingAverage,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ExponentialMovingAverage'>
            }
        }),
        ('weights', {
            'DOMDepth': 1.0,
            'ExponentialMovingAverage': 1.0
        })
    )
