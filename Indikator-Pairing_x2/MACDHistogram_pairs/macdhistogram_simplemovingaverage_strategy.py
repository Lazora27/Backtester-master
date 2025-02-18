import backtrader as bt
from ..base_strategy import FlexibleStrategy

class MACDHistogram_SimpleMovingAverage_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von MACDHistogram und SimpleMovingAverage
    """
    
    params = (
        ('indicators', {
            'MACDHistogram': {
                'class': MACDHistogram,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MACDHistogram'>
            },
            'SimpleMovingAverage': {
                'class': SimpleMovingAverage,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SimpleMovingAverage'>
            }
        }),
        ('weights', {
            'MACDHistogram': 1.0,
            'SimpleMovingAverage': 1.0
        })
    )
