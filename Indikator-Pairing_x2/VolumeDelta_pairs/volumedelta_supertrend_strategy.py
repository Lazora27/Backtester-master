import backtrader as bt
from ..base_strategy import FlexibleStrategy

class VolumeDelta_SuperTrend_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von VolumeDelta und SuperTrend
    """
    
    params = (
        ('indicators', {
            'VolumeDelta': {
                'class': VolumeDelta,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_VolumeDelta'>
            },
            'SuperTrend': {
                'class': SuperTrend,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SuperTrend'>
            }
        }),
        ('weights', {
            'VolumeDelta': 1.0,
            'SuperTrend': 1.0
        })
    )
