import backtrader as bt
from ..base_strategy import FlexibleStrategy

class MLForecast_McClellanSummationIndex_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von MLForecast und McClellanSummationIndex
    """
    
    params = (
        ('indicators', {
            'MLForecast': {
                'class': MLForecast,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MLForecast'>
            },
            'McClellanSummationIndex': {
                'class': McClellanSummationIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_McClellanSummationIndex'>
            }
        }),
        ('weights', {
            'MLForecast': 1.0,
            'McClellanSummationIndex': 1.0
        })
    )
