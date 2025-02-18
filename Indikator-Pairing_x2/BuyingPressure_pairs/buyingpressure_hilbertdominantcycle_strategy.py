import backtrader as bt
from ..base_strategy import FlexibleStrategy

class BuyingPressure_HilbertDominantCycle_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von BuyingPressure und HilbertDominantCycle
    """
    
    params = (
        ('indicators', {
            'BuyingPressure': {
                'class': BuyingPressure,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_BuyingPressure'>
            },
            'HilbertDominantCycle': {
                'class': HilbertDominantCycle,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HilbertDominantCycle'>
            }
        }),
        ('weights', {
            'BuyingPressure': 1.0,
            'HilbertDominantCycle': 1.0
        })
    )
