import backtrader as bt
from ..base_strategy import FlexibleStrategy

class MLForecast_TRIXIndicator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von MLForecast und TRIXIndicator
    """
    
    params = (
        ('indicators', {
            'MLForecast': {
                'class': MLForecast,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MLForecast'>
            },
            'TRIXIndicator': {
                'class': TRIXIndicator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TRIXIndicator'>
            }
        }),
        ('weights', {
            'MLForecast': 1.0,
            'TRIXIndicator': 1.0
        })
    )
