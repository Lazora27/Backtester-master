import backtrader as bt
from ..base_strategy import FlexibleStrategy

class UlcerIndexVolume_SeasonalStrength_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von UlcerIndexVolume und SeasonalStrength
    """
    
    params = (
        ('indicators', {
            'UlcerIndexVolume': {
                'class': UlcerIndexVolume,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_UlcerIndexVolume'>
            },
            'SeasonalStrength': {
                'class': SeasonalStrength,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SeasonalStrength'>
            }
        }),
        ('weights', {
            'UlcerIndexVolume': 1.0,
            'SeasonalStrength': 1.0
        })
    )
