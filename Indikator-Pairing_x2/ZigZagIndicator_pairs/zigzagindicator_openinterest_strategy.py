import backtrader as bt
from ..base_strategy import FlexibleStrategy

class ZigZagIndicator_OpenInterest_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von ZigZagIndicator und OpenInterest
    """
    
    params = (
        ('indicators', {
            'ZigZagIndicator': {
                'class': ZigZagIndicator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ZigZagIndicator'>
            },
            'OpenInterest': {
                'class': OpenInterest,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_OpenInterest'>
            }
        }),
        ('weights', {
            'ZigZagIndicator': 1.0,
            'OpenInterest': 1.0
        })
    )
