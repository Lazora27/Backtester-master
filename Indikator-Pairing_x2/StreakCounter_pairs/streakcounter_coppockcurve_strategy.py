import backtrader as bt
from ..base_strategy import FlexibleStrategy

class StreakCounter_CoppockCurve_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von StreakCounter und CoppockCurve
    """
    
    params = (
        ('indicators', {
            'StreakCounter': {
                'class': StreakCounter,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_StreakCounter'>
            },
            'CoppockCurve': {
                'class': CoppockCurve,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CoppockCurve'>
            }
        }),
        ('weights', {
            'StreakCounter': 1.0,
            'CoppockCurve': 1.0
        })
    )
