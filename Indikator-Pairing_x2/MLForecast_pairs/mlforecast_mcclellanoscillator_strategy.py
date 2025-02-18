import backtrader as bt
from ..base_strategy import FlexibleStrategy

class MLForecast_McClellanOscillator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von MLForecast und McClellanOscillator
    """
    
    params = (
        ('indicators', {
            'MLForecast': {
                'class': MLForecast,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MLForecast'>
            },
            'McClellanOscillator': {
                'class': McClellanOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_McClellanOscillator'>
            }
        }),
        ('weights', {
            'MLForecast': 1.0,
            'McClellanOscillator': 1.0
        })
    )
