import backtrader as bt
from ..base_strategy import FlexibleStrategy

class ZigZagIndicator_SmoothedVolatilityIndicator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von ZigZagIndicator und SmoothedVolatilityIndicator
    """
    
    params = (
        ('indicators', {
            'ZigZagIndicator': {
                'class': ZigZagIndicator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ZigZagIndicator'>
            },
            'SmoothedVolatilityIndicator': {
                'class': SmoothedVolatilityIndicator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SmoothedVolatilityIndicator'>
            }
        }),
        ('weights', {
            'ZigZagIndicator': 1.0,
            'SmoothedVolatilityIndicator': 1.0
        })
    )
