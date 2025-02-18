import backtrader as bt
from ..base_strategy import FlexibleStrategy

class MLForecast_TrueRangeIndicator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von MLForecast und TrueRangeIndicator
    """
    
    params = (
        ('indicators', {
            'MLForecast': {
                'class': MLForecast,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MLForecast'>
            },
            'TrueRangeIndicator': {
                'class': TrueRangeIndicator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TrueRangeIndicator'>
            }
        }),
        ('weights', {
            'MLForecast': 1.0,
            'TrueRangeIndicator': 1.0
        })
    )
