import backtrader as bt
from ..base_strategy import FlexibleStrategy

class KDJIndicator_PercentageVolumeOscillator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von KDJIndicator und PercentageVolumeOscillator
    """
    
    params = (
        ('indicators', {
            'KDJIndicator': {
                'class': KDJIndicator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_KDJIndicator'>
            },
            'PercentageVolumeOscillator': {
                'class': PercentageVolumeOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PercentageVolumeOscillator'>
            }
        }),
        ('weights', {
            'KDJIndicator': 1.0,
            'PercentageVolumeOscillator': 1.0
        })
    )
