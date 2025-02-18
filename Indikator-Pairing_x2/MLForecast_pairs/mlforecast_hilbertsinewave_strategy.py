import backtrader as bt
from ..base_strategy import FlexibleStrategy

class MLForecast_HilbertSinewave_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von MLForecast und HilbertSinewave
    """
    
    params = (
        ('indicators', {
            'MLForecast': {
                'class': MLForecast,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MLForecast'>
            },
            'HilbertSinewave': {
                'class': HilbertSinewave,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HilbertSinewave'>
            }
        }),
        ('weights', {
            'MLForecast': 1.0,
            'HilbertSinewave': 1.0
        })
    )
