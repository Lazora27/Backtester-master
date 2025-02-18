import backtrader as bt
from ..base_strategy import FlexibleStrategy

class McClellanOscillator_ForecastOscillator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von McClellanOscillator und ForecastOscillator
    """
    
    params = (
        ('indicators', {
            'McClellanOscillator': {
                'class': McClellanOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_McClellanOscillator'>
            },
            'ForecastOscillator': {
                'class': ForecastOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ForecastOscillator'>
            }
        }),
        ('weights', {
            'McClellanOscillator': 1.0,
            'ForecastOscillator': 1.0
        })
    )
