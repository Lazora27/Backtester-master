import backtrader as bt
from ..base_strategy import FlexibleStrategy

class DPOCycles_HilbertDominantCycle_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von DPOCycles und HilbertDominantCycle
    """
    
    params = (
        ('indicators', {
            'DPOCycles': {
                'class': DPOCycles,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_DPOCycles'>
            },
            'HilbertDominantCycle': {
                'class': HilbertDominantCycle,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HilbertDominantCycle'>
            }
        }),
        ('weights', {
            'DPOCycles': 1.0,
            'HilbertDominantCycle': 1.0
        })
    )
