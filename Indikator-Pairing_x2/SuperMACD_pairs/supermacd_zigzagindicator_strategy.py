import backtrader as bt
from ..base_strategy import FlexibleStrategy

class SuperMACD_ZigZagIndicator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von SuperMACD und ZigZagIndicator
    """
    
    params = (
        ('indicators', {
            'SuperMACD': {
                'class': SuperMACD,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SuperMACD'>
            },
            'ZigZagIndicator': {
                'class': ZigZagIndicator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ZigZagIndicator'>
            }
        }),
        ('weights', {
            'SuperMACD': 1.0,
            'ZigZagIndicator': 1.0
        })
    )
