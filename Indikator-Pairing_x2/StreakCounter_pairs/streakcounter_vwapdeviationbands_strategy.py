import backtrader as bt
from ..base_strategy import FlexibleStrategy

class StreakCounter_VWAPDeviationBands_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von StreakCounter und VWAPDeviationBands
    """
    
    params = (
        ('indicators', {
            'StreakCounter': {
                'class': StreakCounter,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_StreakCounter'>
            },
            'VWAPDeviationBands': {
                'class': VWAPDeviationBands,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_VWAPDeviationBands'>
            }
        }),
        ('weights', {
            'StreakCounter': 1.0,
            'VWAPDeviationBands': 1.0
        })
    )
