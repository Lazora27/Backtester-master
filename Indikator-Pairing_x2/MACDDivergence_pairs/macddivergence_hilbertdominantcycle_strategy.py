import backtrader as bt
from ..base_strategy import FlexibleStrategy

class MACDDivergence_HilbertDominantCycle_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von MACDDivergence und HilbertDominantCycle
    """
    
    params = (
        ('indicators', {
            'MACDDivergence': {
                'class': MACDDivergence,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MACDDivergence'>
            },
            'HilbertDominantCycle': {
                'class': HilbertDominantCycle,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HilbertDominantCycle'>
            }
        }),
        ('weights', {
            'MACDDivergence': 1.0,
            'HilbertDominantCycle': 1.0
        })
    )
