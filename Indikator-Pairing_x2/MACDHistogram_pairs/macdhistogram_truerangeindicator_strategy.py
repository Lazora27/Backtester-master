import backtrader as bt
from ..base_strategy import FlexibleStrategy

class MACDHistogram_TrueRangeIndicator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von MACDHistogram und TrueRangeIndicator
    """
    
    params = (
        ('indicators', {
            'MACDHistogram': {
                'class': MACDHistogram,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MACDHistogram'>
            },
            'TrueRangeIndicator': {
                'class': TrueRangeIndicator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TrueRangeIndicator'>
            }
        }),
        ('weights', {
            'MACDHistogram': 1.0,
            'TrueRangeIndicator': 1.0
        })
    )
