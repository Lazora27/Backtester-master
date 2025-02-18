import backtrader as bt
from ..base_strategy import FlexibleStrategy

class TimeSeriesForecast_FlowOfFunds_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von TimeSeriesForecast und FlowOfFunds
    """
    
    params = (
        ('indicators', {
            'TimeSeriesForecast': {
                'class': TimeSeriesForecast,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TimeSeriesForecast'>
            },
            'FlowOfFunds': {
                'class': FlowOfFunds,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FlowOfFunds'>
            }
        }),
        ('weights', {
            'TimeSeriesForecast': 1.0,
            'FlowOfFunds': 1.0
        })
    )
