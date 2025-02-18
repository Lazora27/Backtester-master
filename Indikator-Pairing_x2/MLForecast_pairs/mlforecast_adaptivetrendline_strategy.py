import backtrader as bt
from ..base_strategy import FlexibleStrategy

class MLForecast_AdaptiveTrendLine_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von MLForecast und AdaptiveTrendLine
    """
    
    params = (
        ('indicators', {
            'MLForecast': {
                'class': MLForecast,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MLForecast'>
            },
            'AdaptiveTrendLine': {
                'class': AdaptiveTrendLine,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AdaptiveTrendLine'>
            }
        }),
        ('weights', {
            'MLForecast': 1.0,
            'AdaptiveTrendLine': 1.0
        })
    )
