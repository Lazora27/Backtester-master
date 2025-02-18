import backtrader as bt
from ..base_strategy import FlexibleStrategy

class ZigZagIndicator_UlcerIndexVolume_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von ZigZagIndicator und UlcerIndexVolume
    """
    
    params = (
        ('indicators', {
            'ZigZagIndicator': {
                'class': ZigZagIndicator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ZigZagIndicator'>
            },
            'UlcerIndexVolume': {
                'class': UlcerIndexVolume,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_UlcerIndexVolume'>
            }
        }),
        ('weights', {
            'ZigZagIndicator': 1.0,
            'UlcerIndexVolume': 1.0
        })
    )
