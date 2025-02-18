import backtrader as bt
from ..base_strategy import FlexibleStrategy

class MLForecast_HighLowIndex_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von MLForecast und HighLowIndex
    """
    
    params = (
        ('indicators', {
            'MLForecast': {
                'class': MLForecast,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MLForecast'>
            },
            'HighLowIndex': {
                'class': HighLowIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HighLowIndex'>
            }
        }),
        ('weights', {
            'MLForecast': 1.0,
            'HighLowIndex': 1.0
        })
    )
