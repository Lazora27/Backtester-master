import backtrader as bt
from ..base_strategy import FlexibleStrategy

class TickVolume_HilbertDominantCycle_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von TickVolume und HilbertDominantCycle
    """
    
    params = (
        ('indicators', {
            'TickVolume': {
                'class': TickVolume,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TickVolume'>
            },
            'HilbertDominantCycle': {
                'class': HilbertDominantCycle,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HilbertDominantCycle'>
            }
        }),
        ('weights', {
            'TickVolume': 1.0,
            'HilbertDominantCycle': 1.0
        })
    )
