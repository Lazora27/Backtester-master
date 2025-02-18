import backtrader as bt
from ..base_strategy import FlexibleStrategy

class MLForecast_ModifiedATR_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von MLForecast und ModifiedATR
    """
    
    params = (
        ('indicators', {
            'MLForecast': {
                'class': MLForecast,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MLForecast'>
            },
            'ModifiedATR': {
                'class': ModifiedATR,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ModifiedATR'>
            }
        }),
        ('weights', {
            'MLForecast': 1.0,
            'ModifiedATR': 1.0
        })
    )
