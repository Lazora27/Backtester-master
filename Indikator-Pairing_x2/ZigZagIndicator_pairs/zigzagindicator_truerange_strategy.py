import backtrader as bt
from ..base_strategy import FlexibleStrategy

class ZigZagIndicator_TrueRange_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von ZigZagIndicator und TrueRange
    """
    
    params = (
        ('indicators', {
            'ZigZagIndicator': {
                'class': ZigZagIndicator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ZigZagIndicator'>
            },
            'TrueRange': {
                'class': TrueRange,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TrueRange1'>
            }
        }),
        ('weights', {
            'ZigZagIndicator': 1.0,
            'TrueRange': 1.0
        })
    )
