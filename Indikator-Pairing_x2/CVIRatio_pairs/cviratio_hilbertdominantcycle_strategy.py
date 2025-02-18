import backtrader as bt
from ..base_strategy import FlexibleStrategy

class CVIRatio_HilbertDominantCycle_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von CVIRatio und HilbertDominantCycle
    """
    
    params = (
        ('indicators', {
            'CVIRatio': {
                'class': CVIRatio,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CVIRatio'>
            },
            'HilbertDominantCycle': {
                'class': HilbertDominantCycle,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HilbertDominantCycle'>
            }
        }),
        ('weights', {
            'CVIRatio': 1.0,
            'HilbertDominantCycle': 1.0
        })
    )
