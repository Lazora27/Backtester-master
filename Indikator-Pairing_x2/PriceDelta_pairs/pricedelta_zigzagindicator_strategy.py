import backtrader as bt
from ..base_strategy import FlexibleStrategy

class PriceDelta_ZigZagIndicator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von PriceDelta und ZigZagIndicator
    """
    
    params = (
        ('indicators', {
            'PriceDelta': {
                'class': PriceDelta,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PriceDelta'>
            },
            'ZigZagIndicator': {
                'class': ZigZagIndicator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ZigZagIndicator'>
            }
        }),
        ('weights', {
            'PriceDelta': 1.0,
            'ZigZagIndicator': 1.0
        })
    )
