import backtrader as bt
from ..base_strategy import FlexibleStrategy

class MLForecast_CoppockCurve_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von MLForecast und CoppockCurve
    """
    
    params = (
        ('indicators', {
            'MLForecast': {
                'class': MLForecast,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MLForecast'>
            },
            'CoppockCurve': {
                'class': CoppockCurve,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CoppockCurve'>
            }
        }),
        ('weights', {
            'MLForecast': 1.0,
            'CoppockCurve': 1.0
        })
    )
