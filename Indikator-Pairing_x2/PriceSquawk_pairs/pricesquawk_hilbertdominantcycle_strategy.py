import backtrader as bt
from ..base_strategy import FlexibleStrategy

class PriceSquawk_HilbertDominantCycle_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von PriceSquawk und HilbertDominantCycle
    """
    
    params = (
        ('indicators', {
            'PriceSquawk': {
                'class': PriceSquawk,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PriceSquawk'>
            },
            'HilbertDominantCycle': {
                'class': HilbertDominantCycle,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HilbertDominantCycle'>
            }
        }),
        ('weights', {
            'PriceSquawk': 1.0,
            'HilbertDominantCycle': 1.0
        })
    )
