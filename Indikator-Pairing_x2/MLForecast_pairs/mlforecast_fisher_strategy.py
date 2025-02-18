import backtrader as bt
from ..base_strategy import FlexibleStrategy

class MLForecast_Fisher_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von MLForecast und Fisher
    """
    
    params = (
        ('indicators', {
            'MLForecast': {
                'class': MLForecast,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MLForecast'>
            },
            'Fisher': {
                'class': Fisher,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_Fisher'>
            }
        }),
        ('weights', {
            'MLForecast': 1.0,
            'Fisher': 1.0
        })
    )
