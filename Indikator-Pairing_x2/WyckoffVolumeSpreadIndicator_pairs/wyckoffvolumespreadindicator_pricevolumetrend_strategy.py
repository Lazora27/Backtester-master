import backtrader as bt
from ..base_strategy import FlexibleStrategy

class WyckoffVolumeSpreadIndicator_PriceVolumeTrend_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von WyckoffVolumeSpreadIndicator und PriceVolumeTrend
    """
    
    params = (
        ('indicators', {
            'WyckoffVolumeSpreadIndicator': {
                'class': WyckoffVolumeSpreadIndicator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_WyckoffVolumeSpreadIndicator'>
            },
            'PriceVolumeTrend': {
                'class': PriceVolumeTrend,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PriceVolumeTrend'>
            }
        }),
        ('weights', {
            'WyckoffVolumeSpreadIndicator': 1.0,
            'PriceVolumeTrend': 1.0
        })
    )
