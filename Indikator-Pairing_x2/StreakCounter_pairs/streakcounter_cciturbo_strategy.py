import backtrader as bt
from ..base_strategy import FlexibleStrategy

class StreakCounter_CCITurbo_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von StreakCounter und CCITurbo
    """
    
    params = (
        ('indicators', {
            'StreakCounter': {
                'class': StreakCounter,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_StreakCounter'>
            },
            'CCITurbo': {
                'class': CCITurbo,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CCITurbo'>
            }
        }),
        ('weights', {
            'StreakCounter': 1.0,
            'CCITurbo': 1.0
        })
    )
