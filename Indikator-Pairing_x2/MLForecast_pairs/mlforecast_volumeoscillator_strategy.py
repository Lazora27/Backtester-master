import backtrader as bt
from ..base_strategy import FlexibleStrategy

class MLForecast_VolumeOscillator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von MLForecast und VolumeOscillator
    """
    
    params = (
        ('indicators', {
            'MLForecast': {
                'class': MLForecast,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MLForecast'>
            },
            'VolumeOscillator': {
                'class': VolumeOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_VolumeOscillator'>
            }
        }),
        ('weights', {
            'MLForecast': 1.0,
            'VolumeOscillator': 1.0
        })
    )
