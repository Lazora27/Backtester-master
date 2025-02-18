import backtrader as bt
from ..base_strategy import FlexibleStrategy

class MLForecast_TrueRange_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von MLForecast und TrueRange
    """
    
    params = (
        ('indicators', {
            'MLForecast': {
                'class': MLForecast,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MLForecast'>
            },
            'TrueRange': {
                'class': TrueRange,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TrueRange1'>
            }
        }),
        ('weights', {
            'MLForecast': 1.0,
            'TrueRange': 1.0
        })
    )
