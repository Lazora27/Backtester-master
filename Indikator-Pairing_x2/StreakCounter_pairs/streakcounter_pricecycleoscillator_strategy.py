import backtrader as bt
from ..base_strategy import FlexibleStrategy

class StreakCounter_PriceCycleOscillator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von StreakCounter und PriceCycleOscillator
    """
    
    params = (
        ('indicators', {
            'StreakCounter': {
                'class': StreakCounter,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_StreakCounter'>
            },
            'PriceCycleOscillator': {
                'class': PriceCycleOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PriceCycleOscillator'>
            }
        }),
        ('weights', {
            'StreakCounter': 1.0,
            'PriceCycleOscillator': 1.0
        })
    )
