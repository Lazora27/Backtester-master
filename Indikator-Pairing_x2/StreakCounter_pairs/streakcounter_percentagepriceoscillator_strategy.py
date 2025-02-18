import backtrader as bt
from ..base_strategy import FlexibleStrategy

class StreakCounter_PercentagePriceOscillator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von StreakCounter und PercentagePriceOscillator
    """
    
    params = (
        ('indicators', {
            'StreakCounter': {
                'class': StreakCounter,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_StreakCounter'>
            },
            'PercentagePriceOscillator': {
                'class': PercentagePriceOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PercentagePriceOscillator'>
            }
        }),
        ('weights', {
            'StreakCounter': 1.0,
            'PercentagePriceOscillator': 1.0
        })
    )
