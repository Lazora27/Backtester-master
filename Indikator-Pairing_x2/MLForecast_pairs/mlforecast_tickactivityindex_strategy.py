import backtrader as bt
from ..base_strategy import FlexibleStrategy

class MLForecast_TickActivityIndex_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von MLForecast und TickActivityIndex
    """
    
    params = (
        ('indicators', {
            'MLForecast': {
                'class': MLForecast,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MLForecast'>
            },
            'TickActivityIndex': {
                'class': TickActivityIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TickActivityIndex'>
            }
        }),
        ('weights', {
            'MLForecast': 1.0,
            'TickActivityIndex': 1.0
        })
    )
