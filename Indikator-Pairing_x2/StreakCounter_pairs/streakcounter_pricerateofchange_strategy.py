import backtrader as bt
from ..base_strategy import FlexibleStrategy

class StreakCounter_PriceRateOfChange_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von StreakCounter und PriceRateOfChange
    """
    
    params = (
        ('indicators', {
            'StreakCounter': {
                'class': StreakCounter,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_StreakCounter'>
            },
            'PriceRateOfChange': {
                'class': PriceRateOfChange,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PriceRateOfChange'>
            }
        }),
        ('weights', {
            'StreakCounter': 1.0,
            'PriceRateOfChange': 1.0
        })
    )
