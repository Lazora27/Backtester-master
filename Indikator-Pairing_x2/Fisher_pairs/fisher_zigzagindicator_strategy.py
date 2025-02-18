import backtrader as bt
from ..base_strategy import FlexibleStrategy

class Fisher_ZigZagIndicator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von Fisher und ZigZagIndicator
    """
    
    params = (
        ('indicators', {
            'Fisher': {
                'class': Fisher,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_Fisher'>
            },
            'ZigZagIndicator': {
                'class': ZigZagIndicator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ZigZagIndicator'>
            }
        }),
        ('weights', {
            'Fisher': 1.0,
            'ZigZagIndicator': 1.0
        })
    )
