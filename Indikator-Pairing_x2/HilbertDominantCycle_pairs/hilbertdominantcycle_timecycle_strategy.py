import backtrader as bt
from ..base_strategy import FlexibleStrategy

class HilbertDominantCycle_TimeCycle_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von HilbertDominantCycle und TimeCycle
    """
    
    params = (
        ('indicators', {
            'HilbertDominantCycle': {
                'class': HilbertDominantCycle,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HilbertDominantCycle'>
            },
            'TimeCycle': {
                'class': TimeCycle,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TimeCycle'>
            }
        }),
        ('weights', {
            'HilbertDominantCycle': 1.0,
            'TimeCycle': 1.0
        })
    )
