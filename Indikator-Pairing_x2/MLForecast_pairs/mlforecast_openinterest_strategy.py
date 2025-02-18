import backtrader as bt
from ..base_strategy import FlexibleStrategy

class MLForecast_OpenInterest_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von MLForecast und OpenInterest
    """
    
    params = (
        ('indicators', {
            'MLForecast': {
                'class': MLForecast,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MLForecast'>
            },
            'OpenInterest': {
                'class': OpenInterest,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_OpenInterest'>
            }
        }),
        ('weights', {
            'MLForecast': 1.0,
            'OpenInterest': 1.0
        })
    )
