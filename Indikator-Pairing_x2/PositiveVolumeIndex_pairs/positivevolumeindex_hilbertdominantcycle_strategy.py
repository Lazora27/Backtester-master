import backtrader as bt
from ..base_strategy import FlexibleStrategy

class PositiveVolumeIndex_HilbertDominantCycle_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von PositiveVolumeIndex und HilbertDominantCycle
    """
    
    params = (
        ('indicators', {
            'PositiveVolumeIndex': {
                'class': PositiveVolumeIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PositiveVolumeIndex'>
            },
            'HilbertDominantCycle': {
                'class': HilbertDominantCycle,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HilbertDominantCycle'>
            }
        }),
        ('weights', {
            'PositiveVolumeIndex': 1.0,
            'HilbertDominantCycle': 1.0
        })
    )
