import backtrader as bt
from ..base_strategy import FlexibleStrategy

class MACDHistogram_OpenInterest_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von MACDHistogram und OpenInterest
    """
    
    params = (
        ('indicators', {
            'MACDHistogram': {
                'class': MACDHistogram,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MACDHistogram'>
            },
            'OpenInterest': {
                'class': OpenInterest,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_OpenInterest'>
            }
        }),
        ('weights', {
            'MACDHistogram': 1.0,
            'OpenInterest': 1.0
        })
    )
