import backtrader as bt
from ..base_strategy import FlexibleStrategy

class VolumeOscillator_SeasonalStrength_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von VolumeOscillator und SeasonalStrength
    """
    
    params = (
        ('indicators', {
            'VolumeOscillator': {
                'class': VolumeOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_VolumeOscillator'>
            },
            'SeasonalStrength': {
                'class': SeasonalStrength,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SeasonalStrength'>
            }
        }),
        ('weights', {
            'VolumeOscillator': 1.0,
            'SeasonalStrength': 1.0
        })
    )
