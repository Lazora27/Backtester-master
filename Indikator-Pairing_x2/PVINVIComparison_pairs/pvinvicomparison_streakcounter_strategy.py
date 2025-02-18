import backtrader as bt
from ..base_strategy import FlexibleStrategy

class PVINVIComparison_StreakCounter_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von PVINVIComparison und StreakCounter
    """
    
    params = (
        ('indicators', {
            'PVINVIComparison': {
                'class': PVINVIComparison,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PVINVIComparison'>
            },
            'StreakCounter': {
                'class': StreakCounter,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_StreakCounter'>
            }
        }),
        ('weights', {
            'PVINVIComparison': 1.0,
            'StreakCounter': 1.0
        })
    )
