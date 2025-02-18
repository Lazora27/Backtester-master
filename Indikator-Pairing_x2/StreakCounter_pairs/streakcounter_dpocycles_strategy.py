import backtrader as bt
from ..base_strategy import FlexibleStrategy

class StreakCounter_DPOCycles_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von StreakCounter und DPOCycles
    """
    
    params = (
        ('indicators', {
            'StreakCounter': {
                'class': StreakCounter,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_StreakCounter'>
            },
            'DPOCycles': {
                'class': DPOCycles,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_DPOCycles'>
            }
        }),
        ('weights', {
            'StreakCounter': 1.0,
            'DPOCycles': 1.0
        })
    )
