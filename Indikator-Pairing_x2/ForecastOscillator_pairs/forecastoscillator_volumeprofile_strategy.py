import backtrader as bt
from ..base_strategy import FlexibleStrategy

class ForecastOscillator_VolumeProfile_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von ForecastOscillator und VolumeProfile
    """
    
    params = (
        ('indicators', {
            'ForecastOscillator': {
                'class': ForecastOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ForecastOscillator'>
            },
            'VolumeProfile': {
                'class': VolumeProfile,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_VolumeProfile'>
            }
        }),
        ('weights', {
            'ForecastOscillator': 1.0,
            'VolumeProfile': 1.0
        })
    )
