import backtrader as bt
from ..base_strategy import FlexibleStrategy

class RateOfChange_WyckoffVolumeSpreadIndicator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von RateOfChange und WyckoffVolumeSpreadIndicator
    """
    
    params = (
        ('indicators', {
            'RateOfChange': {
                'class': RateOfChange,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_RateOfChange1'>
            },
            'WyckoffVolumeSpreadIndicator': {
                'class': WyckoffVolumeSpreadIndicator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_WyckoffVolumeSpreadIndicator'>
            }
        }),
        ('weights', {
            'RateOfChange': 1.0,
            'WyckoffVolumeSpreadIndicator': 1.0
        })
    )
