import backtrader as bt
from ..base_strategy import FlexibleStrategy

class StreakCounter_LiquidityIndex_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von StreakCounter und LiquidityIndex
    """
    
    params = (
        ('indicators', {
            'StreakCounter': {
                'class': StreakCounter,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_StreakCounter'>
            },
            'LiquidityIndex': {
                'class': LiquidityIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_LiquidityIndex'>
            }
        }),
        ('weights', {
            'StreakCounter': 1.0,
            'LiquidityIndex': 1.0
        })
    )
