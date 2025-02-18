import backtrader as bt
from ..base_strategy import FlexibleStrategy

class MLForecast_UlcerIndex_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von MLForecast und UlcerIndex
    """
    
    params = (
        ('indicators', {
            'MLForecast': {
                'class': MLForecast,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MLForecast'>
            },
            'UlcerIndex': {
                'class': UlcerIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_UlcerIndex'>
            }
        }),
        ('weights', {
            'MLForecast': 1.0,
            'UlcerIndex': 1.0
        })
    )
