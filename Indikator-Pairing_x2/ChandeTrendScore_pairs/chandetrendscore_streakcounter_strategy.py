import backtrader as bt
from ..base_strategy import FlexibleStrategy

class ChandeTrendScore_StreakCounter_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von ChandeTrendScore und StreakCounter
    """
    
    params = (
        ('indicators', {
            'ChandeTrendScore': {
                'class': ChandeTrendScore,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ChandeTrendScore'>
            },
            'StreakCounter': {
                'class': StreakCounter,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_StreakCounter'>
            }
        }),
        ('weights', {
            'ChandeTrendScore': 1.0,
            'StreakCounter': 1.0
        })
    )
