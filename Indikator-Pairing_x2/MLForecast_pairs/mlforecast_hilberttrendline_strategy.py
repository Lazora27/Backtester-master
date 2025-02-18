import backtrader as bt
from ..base_strategy import FlexibleStrategy

class MLForecast_HilbertTrendline_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von MLForecast und HilbertTrendline
    """
    
    params = (
        ('indicators', {
            'MLForecast': {
                'class': MLForecast,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MLForecast'>
            },
            'HilbertTrendline': {
                'class': HilbertTrendline,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HilbertTrendline'>
            }
        }),
        ('weights', {
            'MLForecast': 1.0,
            'HilbertTrendline': 1.0
        })
    )
