import backtrader as bt
from ..base_strategy import FlexibleStrategy

class MLForecast_AwesomeOscillator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von MLForecast und AwesomeOscillator
    """
    
    params = (
        ('indicators', {
            'MLForecast': {
                'class': MLForecast,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MLForecast'>
            },
            'AwesomeOscillator': {
                'class': AwesomeOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AwesomeOscillator1'>
            }
        }),
        ('weights', {
            'MLForecast': 1.0,
            'AwesomeOscillator': 1.0
        })
    )
