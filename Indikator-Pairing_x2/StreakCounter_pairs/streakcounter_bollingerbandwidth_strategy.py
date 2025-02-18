import backtrader as bt
from ..base_strategy import FlexibleStrategy

class StreakCounter_BollingerBandWidth_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von StreakCounter und BollingerBandWidth
    """
    
    params = (
        ('indicators', {
            'StreakCounter': {
                'class': StreakCounter,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_StreakCounter'>
            },
            'BollingerBandWidth': {
                'class': BollingerBandWidth,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_BollingerBandWidth'>
            }
        }),
        ('weights', {
            'StreakCounter': 1.0,
            'BollingerBandWidth': 1.0
        })
    )
