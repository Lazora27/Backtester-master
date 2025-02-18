import backtrader as bt
from ..base_strategy import FlexibleStrategy

class StreakCounter_FisherTransform_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von StreakCounter und FisherTransform
    """
    
    params = (
        ('indicators', {
            'StreakCounter': {
                'class': StreakCounter,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_StreakCounter'>
            },
            'FisherTransform': {
                'class': FisherTransform,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FisherTransform'>
            }
        }),
        ('weights', {
            'StreakCounter': 1.0,
            'FisherTransform': 1.0
        })
    )
