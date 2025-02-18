import backtrader as bt
from ..base_strategy import FlexibleStrategy

class ZigZagIndicator_UlcerIndex_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von ZigZagIndicator und UlcerIndex
    """
    
    params = (
        ('indicators', {
            'ZigZagIndicator': {
                'class': ZigZagIndicator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ZigZagIndicator'>
            },
            'UlcerIndex': {
                'class': UlcerIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_UlcerIndex'>
            }
        }),
        ('weights', {
            'ZigZagIndicator': 1.0,
            'UlcerIndex': 1.0
        })
    )
