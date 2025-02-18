import backtrader as bt
from ..base_strategy import FlexibleStrategy

class MLForecast_TrendCycles_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von MLForecast und TrendCycles
    """
    
    params = (
        ('indicators', {
            'MLForecast': {
                'class': MLForecast,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MLForecast'>
            },
            'TrendCycles': {
                'class': TrendCycles,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TrendCycles'>
            }
        }),
        ('weights', {
            'MLForecast': 1.0,
            'TrendCycles': 1.0
        })
    )
