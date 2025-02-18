import backtrader as bt
from ..base_strategy import FlexibleStrategy

class StreakCounter_HerrickPayoffIndex_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von StreakCounter und HerrickPayoffIndex
    """
    
    params = (
        ('indicators', {
            'StreakCounter': {
                'class': StreakCounter,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_StreakCounter'>
            },
            'HerrickPayoffIndex': {
                'class': HerrickPayoffIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HerrickPayoffIndex'>
            }
        }),
        ('weights', {
            'StreakCounter': 1.0,
            'HerrickPayoffIndex': 1.0
        })
    )
