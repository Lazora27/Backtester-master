import backtrader as bt
from ..base_strategy import FlexibleStrategy

class RateOfChange_HilbertDominantCycle_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von RateOfChange und HilbertDominantCycle
    """
    
    params = (
        ('indicators', {
            'RateOfChange': {
                'class': RateOfChange,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_RateOfChange1'>
            },
            'HilbertDominantCycle': {
                'class': HilbertDominantCycle,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HilbertDominantCycle'>
            }
        }),
        ('weights', {
            'RateOfChange': 1.0,
            'HilbertDominantCycle': 1.0
        })
    )
