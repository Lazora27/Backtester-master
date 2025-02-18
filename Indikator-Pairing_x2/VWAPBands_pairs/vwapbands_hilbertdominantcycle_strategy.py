import backtrader as bt
from ..base_strategy import FlexibleStrategy

class VWAPBands_HilbertDominantCycle_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von VWAPBands und HilbertDominantCycle
    """
    
    params = (
        ('indicators', {
            'VWAPBands': {
                'class': VWAPBands,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_VWAPBands'>
            },
            'HilbertDominantCycle': {
                'class': HilbertDominantCycle,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HilbertDominantCycle'>
            }
        }),
        ('weights', {
            'VWAPBands': 1.0,
            'HilbertDominantCycle': 1.0
        })
    )
