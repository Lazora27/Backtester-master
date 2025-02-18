import backtrader as bt
from ..base_strategy import FlexibleStrategy

class SmoothedRSI_ExponentialMovingAverage_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von SmoothedRSI und ExponentialMovingAverage
    """
    
    params = (
        ('indicators', {
            'SmoothedRSI': {
                'class': SmoothedRSI,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SmoothedRSI'>
            },
            'ExponentialMovingAverage': {
                'class': ExponentialMovingAverage,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ExponentialMovingAverage'>
            }
        }),
        ('weights', {
            'SmoothedRSI': 1.0,
            'ExponentialMovingAverage': 1.0
        })
    )
