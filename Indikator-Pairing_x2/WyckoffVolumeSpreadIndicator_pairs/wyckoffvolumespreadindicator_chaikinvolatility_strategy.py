import backtrader as bt
from ..base_strategy import FlexibleStrategy

class WyckoffVolumeSpreadIndicator_ChaikinVolatility_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von WyckoffVolumeSpreadIndicator und ChaikinVolatility
    """
    
    params = (
        ('indicators', {
            'WyckoffVolumeSpreadIndicator': {
                'class': WyckoffVolumeSpreadIndicator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_WyckoffVolumeSpreadIndicator'>
            },
            'ChaikinVolatility': {
                'class': ChaikinVolatility,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ChaikinVolatility'>
            }
        }),
        ('weights', {
            'WyckoffVolumeSpreadIndicator': 1.0,
            'ChaikinVolatility': 1.0
        })
    )
