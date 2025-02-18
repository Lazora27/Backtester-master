import backtrader as bt
from ..base_strategy import FlexibleStrategy

class CVIRatio_StreakCounter_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von CVIRatio und StreakCounter
    """
    
    params = (
        ('indicators', {
            'CVIRatio': {
                'class': CVIRatio,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CVIRatio'>
            },
            'StreakCounter': {
                'class': StreakCounter,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_StreakCounter'>
            }
        }),
        ('weights', {
            'CVIRatio': 1.0,
            'StreakCounter': 1.0
        })
    )
