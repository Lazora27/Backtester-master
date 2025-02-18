import backtrader as bt
from ..base_strategy import FlexibleStrategy

class SuperTrend_VolumeTrendIndicator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von SuperTrend und VolumeTrendIndicator
    """
    
    params = (
        ('indicators', {
            'SuperTrend': {
                'class': SuperTrend,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SuperTrend'>
            },
            'VolumeTrendIndicator': {
                'class': VolumeTrendIndicator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_VolumeTrendIndicator'>
            }
        }),
        ('weights', {
            'SuperTrend': 1.0,
            'VolumeTrendIndicator': 1.0
        })
    )
