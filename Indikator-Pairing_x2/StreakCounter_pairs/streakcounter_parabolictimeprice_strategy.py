import backtrader as bt
from ..base_strategy import FlexibleStrategy

class StreakCounter_ParabolicTimePrice_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von StreakCounter und ParabolicTimePrice
    """
    
    params = (
        ('indicators', {
            'StreakCounter': {
                'class': StreakCounter,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_StreakCounter'>
            },
            'ParabolicTimePrice': {
                'class': ParabolicTimePrice,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ParabolicTimePrice'>
            }
        }),
        ('weights', {
            'StreakCounter': 1.0,
            'ParabolicTimePrice': 1.0
        })
    )
