import backtrader as bt
from ..base_strategy import FlexibleStrategy

class MLForecast_AutoFibonacci_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von MLForecast und AutoFibonacci
    """
    
    params = (
        ('indicators', {
            'MLForecast': {
                'class': MLForecast,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MLForecast'>
            },
            'AutoFibonacci': {
                'class': AutoFibonacci,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AutoFibonacci'>
            }
        }),
        ('weights', {
            'MLForecast': 1.0,
            'AutoFibonacci': 1.0
        })
    )
