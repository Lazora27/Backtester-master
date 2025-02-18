import backtrader as bt
from ..base_strategy import FlexibleStrategy

class ForecastOscillator_WyckoffVolumeSpreadIndicator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von ForecastOscillator und WyckoffVolumeSpreadIndicator
    """
    
    params = (
        ('indicators', {
            'ForecastOscillator': {
                'class': ForecastOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ForecastOscillator'>
            },
            'WyckoffVolumeSpreadIndicator': {
                'class': WyckoffVolumeSpreadIndicator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_WyckoffVolumeSpreadIndicator'>
            }
        }),
        ('weights', {
            'ForecastOscillator': 1.0,
            'WyckoffVolumeSpreadIndicator': 1.0
        })
    )
