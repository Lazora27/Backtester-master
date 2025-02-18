import backtrader as bt
from ..base_strategy import FlexibleStrategy

class FourierCycleFilter_HilbertDominantCycle_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von FourierCycleFilter und HilbertDominantCycle
    """
    
    params = (
        ('indicators', {
            'FourierCycleFilter': {
                'class': FourierCycleFilter,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FourierCycleFilter'>
            },
            'HilbertDominantCycle': {
                'class': HilbertDominantCycle,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HilbertDominantCycle'>
            }
        }),
        ('weights', {
            'FourierCycleFilter': 1.0,
            'HilbertDominantCycle': 1.0
        })
    )
