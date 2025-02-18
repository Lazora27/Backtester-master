import backtrader as bt
from ..base_strategy import FlexibleStrategy

class ZigZagIndicator_BuyingPressure_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von ZigZagIndicator und BuyingPressure
    """
    
    params = (
        ('indicators', {
            'ZigZagIndicator': {
                'class': ZigZagIndicator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ZigZagIndicator'>
            },
            'BuyingPressure': {
                'class': BuyingPressure,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_BuyingPressure'>
            }
        }),
        ('weights', {
            'ZigZagIndicator': 1.0,
            'BuyingPressure': 1.0
        })
    )
