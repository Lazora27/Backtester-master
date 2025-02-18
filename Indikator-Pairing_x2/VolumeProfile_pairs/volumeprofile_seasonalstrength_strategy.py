import backtrader as bt
from ..base_strategy import FlexibleStrategy

class VolumeProfile_SeasonalStrength_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von VolumeProfile und SeasonalStrength
    """
    
    params = (
        ('indicators', {
            'VolumeProfile': {
                'class': VolumeProfile,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_VolumeProfile'>
            },
            'SeasonalStrength': {
                'class': SeasonalStrength,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SeasonalStrength'>
            }
        }),
        ('weights', {
            'VolumeProfile': 1.0,
            'SeasonalStrength': 1.0
        })
    )
