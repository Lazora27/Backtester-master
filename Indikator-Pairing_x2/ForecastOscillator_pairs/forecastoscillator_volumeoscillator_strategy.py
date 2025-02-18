import backtrader as bt
from ..base_strategy import FlexibleStrategy

class ForecastOscillator_VolumeOscillator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von ForecastOscillator und VolumeOscillator
    """
    
    params = (
        ('indicators', {
            'ForecastOscillator': {
                'class': ForecastOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ForecastOscillator'>
            },
            'VolumeOscillator': {
                'class': VolumeOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_VolumeOscillator'>
            }
        }),
        ('weights', {
            'ForecastOscillator': 1.0,
            'VolumeOscillator': 1.0
        })
    )
