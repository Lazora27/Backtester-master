import backtrader as bt
from ..base_strategy import FlexibleStrategy

class PriceSquawk_ZigZagIndicator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von PriceSquawk und ZigZagIndicator
    """
    
    params = (
        ('indicators', {
            'PriceSquawk': {
                'class': PriceSquawk,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PriceSquawk'>
            },
            'ZigZagIndicator': {
                'class': ZigZagIndicator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ZigZagIndicator'>
            }
        }),
        ('weights', {
            'PriceSquawk': 1.0,
            'ZigZagIndicator': 1.0
        })
    )
