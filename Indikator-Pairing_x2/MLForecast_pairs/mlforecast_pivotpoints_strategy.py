import backtrader as bt
from ..base_strategy import FlexibleStrategy

class MLForecast_PivotPoints_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von MLForecast und PivotPoints
    """
    
    params = (
        ('indicators', {
            'MLForecast': {
                'class': MLForecast,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MLForecast'>
            },
            'PivotPoints': {
                'class': PivotPoints,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PivotPoints'>
            }
        }),
        ('weights', {
            'MLForecast': 1.0,
            'PivotPoints': 1.0
        })
    )
