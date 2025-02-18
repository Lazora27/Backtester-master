import backtrader as bt
from ..base_strategy import FlexibleStrategy

class StreakCounter_VolumeFlowIndicator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von StreakCounter und VolumeFlowIndicator
    """
    
    params = (
        ('indicators', {
            'StreakCounter': {
                'class': StreakCounter,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_StreakCounter'>
            },
            'VolumeFlowIndicator': {
                'class': VolumeFlowIndicator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_VolumeFlowIndicator'>
            }
        }),
        ('weights', {
            'StreakCounter': 1.0,
            'VolumeFlowIndicator': 1.0
        })
    )
