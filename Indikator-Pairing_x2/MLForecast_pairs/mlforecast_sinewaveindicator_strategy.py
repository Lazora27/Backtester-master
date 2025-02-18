import backtrader as bt
from ..base_strategy import FlexibleStrategy

class MLForecast_SineWaveIndicator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von MLForecast und SineWaveIndicator
    """
    
    params = (
        ('indicators', {
            'MLForecast': {
                'class': MLForecast,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MLForecast'>
            },
            'SineWaveIndicator': {
                'class': SineWaveIndicator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SineWaveIndicator'>
            }
        }),
        ('weights', {
            'MLForecast': 1.0,
            'SineWaveIndicator': 1.0
        })
    )
