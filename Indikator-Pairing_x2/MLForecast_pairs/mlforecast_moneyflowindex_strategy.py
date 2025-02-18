import backtrader as bt
from ..base_strategy import FlexibleStrategy

class MLForecast_MoneyFlowIndex_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von MLForecast und MoneyFlowIndex
    """
    
    params = (
        ('indicators', {
            'MLForecast': {
                'class': MLForecast,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MLForecast'>
            },
            'MoneyFlowIndex': {
                'class': MoneyFlowIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MoneyFlowIndex'>
            }
        }),
        ('weights', {
            'MLForecast': 1.0,
            'MoneyFlowIndex': 1.0
        })
    )
