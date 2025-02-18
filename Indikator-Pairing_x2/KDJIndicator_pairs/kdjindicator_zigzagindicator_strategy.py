import backtrader as bt
from ..base_strategy import FlexibleStrategy

class KDJIndicator_ZigZagIndicator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von KDJIndicator und ZigZagIndicator
    """
    
    params = (
        ('indicators', {
            'KDJIndicator': {
                'class': KDJIndicator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_KDJIndicator'>
            },
            'ZigZagIndicator': {
                'class': ZigZagIndicator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ZigZagIndicator'>
            }
        }),
        ('weights', {
            'KDJIndicator': 1.0,
            'ZigZagIndicator': 1.0
        })
    )
