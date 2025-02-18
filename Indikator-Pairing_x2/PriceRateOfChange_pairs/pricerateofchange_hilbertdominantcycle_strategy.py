import backtrader as bt
from ..base_strategy import FlexibleStrategy

class PriceRateOfChange_HilbertDominantCycle_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von PriceRateOfChange und HilbertDominantCycle
    """
    
    params = (
        ('indicators', {
            'PriceRateOfChange': {
                'class': PriceRateOfChange,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PriceRateOfChange'>
            },
            'HilbertDominantCycle': {
                'class': HilbertDominantCycle,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HilbertDominantCycle'>
            }
        }),
        ('weights', {
            'PriceRateOfChange': 1.0,
            'HilbertDominantCycle': 1.0
        })
    )
