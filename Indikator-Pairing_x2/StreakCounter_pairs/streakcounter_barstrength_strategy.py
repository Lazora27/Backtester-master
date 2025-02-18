import backtrader as bt
from ..base_strategy import FlexibleStrategy

class StreakCounter_BarStrength_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von StreakCounter und BarStrength
    """
    
    params = (
        ('indicators', {
            'StreakCounter': {
                'class': StreakCounter,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_StreakCounter'>
            },
            'BarStrength': {
                'class': BarStrength,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_BarStrength'>
            }
        }),
        ('weights', {
            'StreakCounter': 1.0,
            'BarStrength': 1.0
        })
    )
