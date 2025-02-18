import backtrader as bt
from ..base_strategy import FlexibleStrategy

class MACDHistogram_ExponentialMovingAverage_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von MACDHistogram und ExponentialMovingAverage
    """
    
    params = (
        ('indicators', {
            'MACDHistogram': {
                'class': MACDHistogram,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MACDHistogram'>
            },
            'ExponentialMovingAverage': {
                'class': ExponentialMovingAverage,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ExponentialMovingAverage'>
            }
        }),
        ('weights', {
            'MACDHistogram': 1.0,
            'ExponentialMovingAverage': 1.0
        })
    )
