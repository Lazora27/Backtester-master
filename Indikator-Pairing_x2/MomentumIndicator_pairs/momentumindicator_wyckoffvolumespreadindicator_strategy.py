import backtrader as bt
from ..base_strategy import FlexibleStrategy

class MomentumIndicator_WyckoffVolumeSpreadIndicator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von MomentumIndicator und WyckoffVolumeSpreadIndicator
    """
    
    params = (
        ('indicators', {
            'MomentumIndicator': {
                'class': MomentumIndicator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MomentumIndicator'>
            },
            'WyckoffVolumeSpreadIndicator': {
                'class': WyckoffVolumeSpreadIndicator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_WyckoffVolumeSpreadIndicator'>
            }
        }),
        ('weights', {
            'MomentumIndicator': 1.0,
            'WyckoffVolumeSpreadIndicator': 1.0
        })
    )
