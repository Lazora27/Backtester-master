import backtrader as bt
from ..base_strategy import FlexibleStrategy

class MLForecast_HilbertDominantCycle_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von MLForecast und HilbertDominantCycle
    """
    
    params = (
        ('indicators', {
            'MLForecast': {
                'class': MLForecast,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MLForecast'>
            },
            'HilbertDominantCycle': {
                'class': HilbertDominantCycle,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HilbertDominantCycle'>
            }
        }),
        ('weights', {
            'MLForecast': 1.0,
            'HilbertDominantCycle': 1.0
        })
    )
