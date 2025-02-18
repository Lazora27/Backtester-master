import backtrader as bt
from ..base_strategy import FlexibleStrategy

class MACDHistogram_HullMovingAverage_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von MACDHistogram und HullMovingAverage
    """
    
    params = (
        ('indicators', {
            'MACDHistogram': {
                'class': MACDHistogram,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MACDHistogram'>
            },
            'HullMovingAverage': {
                'class': HullMovingAverage,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HullMovingAverage'>
            }
        }),
        ('weights', {
            'MACDHistogram': 1.0,
            'HullMovingAverage': 1.0
        })
    )
