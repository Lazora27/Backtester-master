import backtrader as bt
from ..base_strategy import FlexibleStrategy

class MLForecast_SineWaveOscillator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von MLForecast und SineWaveOscillator
    """
    
    params = (
        ('indicators', {
            'MLForecast': {
                'class': MLForecast,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MLForecast'>
            },
            'SineWaveOscillator': {
                'class': SineWaveOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SineWaveOscillator'>
            }
        }),
        ('weights', {
            'MLForecast': 1.0,
            'SineWaveOscillator': 1.0
        })
    )
