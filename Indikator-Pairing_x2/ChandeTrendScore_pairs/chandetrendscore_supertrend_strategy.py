import backtrader as bt
from ..base_strategy import FlexibleStrategy

class ChandeTrendScore_SuperTrend_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von ChandeTrendScore und SuperTrend
    """
    
    params = (
        ('indicators', {
            'ChandeTrendScore': {
                'class': ChandeTrendScore,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ChandeTrendScore'>
            },
            'SuperTrend': {
                'class': SuperTrend,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SuperTrend'>
            }
        }),
        ('weights', {
            'ChandeTrendScore': 1.0,
            'SuperTrend': 1.0
        })
    )
