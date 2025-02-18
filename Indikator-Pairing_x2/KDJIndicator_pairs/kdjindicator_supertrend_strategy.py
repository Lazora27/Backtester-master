import backtrader as bt
from ..base_strategy import FlexibleStrategy

class KDJIndicator_SuperTrend_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von KDJIndicator und SuperTrend
    """
    
    params = (
        ('indicators', {
            'KDJIndicator': {
                'class': KDJIndicator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_KDJIndicator'>
            },
            'SuperTrend': {
                'class': SuperTrend,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SuperTrend'>
            }
        }),
        ('weights', {
            'KDJIndicator': 1.0,
            'SuperTrend': 1.0
        })
    )
