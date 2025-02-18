import backtrader as bt
from ..base_strategy import FlexibleStrategy

class MLForecast_TickIndex_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von MLForecast und TickIndex
    """
    
    params = (
        ('indicators', {
            'MLForecast': {
                'class': MLForecast,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MLForecast'>
            },
            'TickIndex': {
                'class': TickIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TickIndex'>
            }
        }),
        ('weights', {
            'MLForecast': 1.0,
            'TickIndex': 1.0
        })
    )
