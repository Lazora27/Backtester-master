import backtrader as bt
from ..base_strategy import FlexibleStrategy

class MLForecast_MACDHistogram_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von MLForecast und MACDHistogram
    """
    
    params = (
        ('indicators', {
            'MLForecast': {
                'class': MLForecast,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MLForecast'>
            },
            'MACDHistogram': {
                'class': MACDHistogram,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MACDHistogram'>
            }
        }),
        ('weights', {
            'MLForecast': 1.0,
            'MACDHistogram': 1.0
        })
    )
