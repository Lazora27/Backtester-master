import backtrader as bt
from ..base_strategy import FlexibleStrategy

class MLForecast_GannSquareReversal_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von MLForecast und GannSquareReversal
    """
    
    params = (
        ('indicators', {
            'MLForecast': {
                'class': MLForecast,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MLForecast'>
            },
            'GannSquareReversal': {
                'class': GannSquareReversal,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_GannSquareReversal'>
            }
        }),
        ('weights', {
            'MLForecast': 1.0,
            'GannSquareReversal': 1.0
        })
    )
