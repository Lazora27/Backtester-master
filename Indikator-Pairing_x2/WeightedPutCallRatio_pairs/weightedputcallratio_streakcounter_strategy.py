import backtrader as bt
from ..base_strategy import FlexibleStrategy

class WeightedPutCallRatio_StreakCounter_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von WeightedPutCallRatio und StreakCounter
    """
    
    params = (
        ('indicators', {
            'WeightedPutCallRatio': {
                'class': WeightedPutCallRatio,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_WeightedPutCallRatio'>
            },
            'StreakCounter': {
                'class': StreakCounter,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_StreakCounter'>
            }
        }),
        ('weights', {
            'WeightedPutCallRatio': 1.0,
            'StreakCounter': 1.0
        })
    )
