import backtrader as bt
from ..base_strategy import FlexibleStrategy

class MACDHistogram_TRIXIndicator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von MACDHistogram und TRIXIndicator
    """
    
    params = (
        ('indicators', {
            'MACDHistogram': {
                'class': MACDHistogram,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MACDHistogram'>
            },
            'TRIXIndicator': {
                'class': TRIXIndicator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TRIXIndicator'>
            }
        }),
        ('weights', {
            'MACDHistogram': 1.0,
            'TRIXIndicator': 1.0
        })
    )
