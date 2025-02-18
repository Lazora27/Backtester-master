import backtrader as bt
from ..base_strategy import FlexibleStrategy

class ForecastOscillator_VolumeDelta_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von ForecastOscillator und VolumeDelta
    """
    
    params = (
        ('indicators', {
            'ForecastOscillator': {
                'class': ForecastOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ForecastOscillator'>
            },
            'VolumeDelta': {
                'class': VolumeDelta,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_VolumeDelta'>
            }
        }),
        ('weights', {
            'ForecastOscillator': 1.0,
            'VolumeDelta': 1.0
        })
    )
