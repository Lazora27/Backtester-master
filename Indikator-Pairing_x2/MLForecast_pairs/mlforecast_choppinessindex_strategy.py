import backtrader as bt
from ..base_strategy import FlexibleStrategy

class MLForecast_ChoppinessIndex_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von MLForecast und ChoppinessIndex
    """
    
    params = (
        ('indicators', {
            'MLForecast': {
                'class': MLForecast,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MLForecast'>
            },
            'ChoppinessIndex': {
                'class': ChoppinessIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ChoppinessIndex'>
            }
        }),
        ('weights', {
            'MLForecast': 1.0,
            'ChoppinessIndex': 1.0
        })
    )
