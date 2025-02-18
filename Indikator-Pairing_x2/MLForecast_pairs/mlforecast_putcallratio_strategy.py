import backtrader as bt
from ..base_strategy import FlexibleStrategy

class MLForecast_PutCallRatio_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von MLForecast und PutCallRatio
    """
    
    params = (
        ('indicators', {
            'MLForecast': {
                'class': MLForecast,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MLForecast'>
            },
            'PutCallRatio': {
                'class': PutCallRatio,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PutCallRatio1'>
            }
        }),
        ('weights', {
            'MLForecast': 1.0,
            'PutCallRatio': 1.0
        })
    )
