import backtrader as bt
from ..base_strategy import FlexibleStrategy

class StreakCounter_EhlersFisherTransform_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von StreakCounter und EhlersFisherTransform
    """
    
    params = (
        ('indicators', {
            'StreakCounter': {
                'class': StreakCounter,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_StreakCounter'>
            },
            'EhlersFisherTransform': {
                'class': EhlersFisherTransform,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_EhlersFisherTransform'>
            }
        }),
        ('weights', {
            'StreakCounter': 1.0,
            'EhlersFisherTransform': 1.0
        })
    )
