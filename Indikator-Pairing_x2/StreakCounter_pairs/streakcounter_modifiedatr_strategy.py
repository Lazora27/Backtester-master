import backtrader as bt
from ..base_strategy import FlexibleStrategy

class StreakCounter_ModifiedATR_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von StreakCounter und ModifiedATR
    """
    
    params = (
        ('indicators', {
            'StreakCounter': {
                'class': StreakCounter,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_StreakCounter'>
            },
            'ModifiedATR': {
                'class': ModifiedATR,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ModifiedATR'>
            }
        }),
        ('weights', {
            'StreakCounter': 1.0,
            'ModifiedATR': 1.0
        })
    )
