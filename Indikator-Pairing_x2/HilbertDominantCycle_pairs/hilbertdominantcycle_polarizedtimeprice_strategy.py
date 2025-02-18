import backtrader as bt
from ..base_strategy import FlexibleStrategy

class HilbertDominantCycle_PolarizedTimePrice_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von HilbertDominantCycle und PolarizedTimePrice
    """
    
    params = (
        ('indicators', {
            'HilbertDominantCycle': {
                'class': HilbertDominantCycle,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HilbertDominantCycle'>
            },
            'PolarizedTimePrice': {
                'class': PolarizedTimePrice,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PolarizedTimePrice'>
            }
        }),
        ('weights', {
            'HilbertDominantCycle': 1.0,
            'PolarizedTimePrice': 1.0
        })
    )
