import backtrader as bt
from ..base_strategy import FlexibleStrategy

class MLForecast_DOMDepth_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von MLForecast und DOMDepth
    """
    
    params = (
        ('indicators', {
            'MLForecast': {
                'class': MLForecast,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MLForecast'>
            },
            'DOMDepth': {
                'class': DOMDepth,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_DOMDepth'>
            }
        }),
        ('weights', {
            'MLForecast': 1.0,
            'DOMDepth': 1.0
        })
    )
