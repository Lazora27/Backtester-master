import backtrader as bt
from ..base_strategy import FlexibleStrategy

class MLForecast_GannSquares_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von MLForecast und GannSquares
    """
    
    params = (
        ('indicators', {
            'MLForecast': {
                'class': MLForecast,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MLForecast'>
            },
            'GannSquares': {
                'class': GannSquares,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_GannSquares'>
            }
        }),
        ('weights', {
            'MLForecast': 1.0,
            'GannSquares': 1.0
        })
    )
