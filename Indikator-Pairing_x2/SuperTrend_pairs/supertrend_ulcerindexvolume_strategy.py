import backtrader as bt
from ..base_strategy import FlexibleStrategy

class SuperTrend_UlcerIndexVolume_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von SuperTrend und UlcerIndexVolume
    """
    
    params = (
        ('indicators', {
            'SuperTrend': {
                'class': SuperTrend,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SuperTrend'>
            },
            'UlcerIndexVolume': {
                'class': UlcerIndexVolume,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_UlcerIndexVolume'>
            }
        }),
        ('weights', {
            'SuperTrend': 1.0,
            'UlcerIndexVolume': 1.0
        })
    )
