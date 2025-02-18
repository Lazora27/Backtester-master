import backtrader as bt
from ..base_strategy import FlexibleStrategy

class StreakCounter_MomentumTrendStrength_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von StreakCounter und MomentumTrendStrength
    """
    
    params = (
        ('indicators', {
            'StreakCounter': {
                'class': StreakCounter,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_StreakCounter'>
            },
            'MomentumTrendStrength': {
                'class': MomentumTrendStrength,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MomentumTrendStrength'>
            }
        }),
        ('weights', {
            'StreakCounter': 1.0,
            'MomentumTrendStrength': 1.0
        })
    )
