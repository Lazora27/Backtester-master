import backtrader as bt
from ..base_strategy import FlexibleStrategy

class MACDHistogram_RainbowMovingAverage_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von MACDHistogram und RainbowMovingAverage
    """
    
    params = (
        ('indicators', {
            'MACDHistogram': {
                'class': MACDHistogram,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MACDHistogram'>
            },
            'RainbowMovingAverage': {
                'class': RainbowMovingAverage,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_RainbowMovingAverage'>
            }
        }),
        ('weights', {
            'MACDHistogram': 1.0,
            'RainbowMovingAverage': 1.0
        })
    )
