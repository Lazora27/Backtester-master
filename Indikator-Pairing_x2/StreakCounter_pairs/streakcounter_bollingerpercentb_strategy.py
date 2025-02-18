import backtrader as bt
from ..base_strategy import FlexibleStrategy

class StreakCounter_BollingerPercentB_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von StreakCounter und BollingerPercentB
    """
    
    params = (
        ('indicators', {
            'StreakCounter': {
                'class': StreakCounter,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_StreakCounter'>
            },
            'BollingerPercentB': {
                'class': BollingerPercentB,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_BollingerPercentB'>
            }
        }),
        ('weights', {
            'StreakCounter': 1.0,
            'BollingerPercentB': 1.0
        })
    )
