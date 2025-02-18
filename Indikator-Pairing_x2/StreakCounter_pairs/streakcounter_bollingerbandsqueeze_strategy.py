import backtrader as bt
from ..base_strategy import FlexibleStrategy

class StreakCounter_BollingerBandSqueeze_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von StreakCounter und BollingerBandSqueeze
    """
    
    params = (
        ('indicators', {
            'StreakCounter': {
                'class': StreakCounter,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_StreakCounter'>
            },
            'BollingerBandSqueeze': {
                'class': BollingerBandSqueeze,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_BollingerBandSqueeze'>
            }
        }),
        ('weights', {
            'StreakCounter': 1.0,
            'BollingerBandSqueeze': 1.0
        })
    )
