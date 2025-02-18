import backtrader as bt
from ..base_strategy import FlexibleStrategy

class MLForecast_HighLowDifference_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von MLForecast und HighLowDifference
    """
    
    params = (
        ('indicators', {
            'MLForecast': {
                'class': MLForecast,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MLForecast'>
            },
            'HighLowDifference': {
                'class': HighLowDifference,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HighLowDifference'>
            }
        }),
        ('weights', {
            'MLForecast': 1.0,
            'HighLowDifference': 1.0
        })
    )
