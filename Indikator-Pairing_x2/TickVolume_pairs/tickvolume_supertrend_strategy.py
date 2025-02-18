import backtrader as bt
from ..base_strategy import FlexibleStrategy

class TickVolume_SuperTrend_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von TickVolume und SuperTrend
    """
    
    params = (
        ('indicators', {
            'TickVolume': {
                'class': TickVolume,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TickVolume'>
            },
            'SuperTrend': {
                'class': SuperTrend,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SuperTrend'>
            }
        }),
        ('weights', {
            'TickVolume': 1.0,
            'SuperTrend': 1.0
        })
    )
