import backtrader as bt
from ..base_strategy import FlexibleStrategy

class StreakCounter_BollingerBands_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von StreakCounter und BollingerBands
    """
    
    params = (
        ('indicators', {
            'StreakCounter': {
                'class': StreakCounter,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_StreakCounter'>
            },
            'BollingerBands': {
                'class': BollingerBands,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_BollingerBands1'>
            }
        }),
        ('weights', {
            'StreakCounter': 1.0,
            'BollingerBands': 1.0
        })
    )
