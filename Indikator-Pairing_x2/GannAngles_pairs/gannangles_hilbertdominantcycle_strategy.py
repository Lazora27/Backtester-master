import backtrader as bt
from ..base_strategy import FlexibleStrategy

class GannAngles_HilbertDominantCycle_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von GannAngles und HilbertDominantCycle
    """
    
    params = (
        ('indicators', {
            'GannAngles': {
                'class': GannAngles,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_GannAngles1'>
            },
            'HilbertDominantCycle': {
                'class': HilbertDominantCycle,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HilbertDominantCycle'>
            }
        }),
        ('weights', {
            'GannAngles': 1.0,
            'HilbertDominantCycle': 1.0
        })
    )
