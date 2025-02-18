import backtrader as bt
from ..base_strategy import FlexibleStrategy

class MLForecast_FlowOfFunds_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von MLForecast und FlowOfFunds
    """
    
    params = (
        ('indicators', {
            'MLForecast': {
                'class': MLForecast,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MLForecast'>
            },
            'FlowOfFunds': {
                'class': FlowOfFunds,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FlowOfFunds'>
            }
        }),
        ('weights', {
            'MLForecast': 1.0,
            'FlowOfFunds': 1.0
        })
    )
