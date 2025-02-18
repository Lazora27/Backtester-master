import backtrader as bt
from ..base_strategy import FlexibleStrategy

class BradleySiderograph_HilbertDominantCycle_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von BradleySiderograph und HilbertDominantCycle
    """
    
    params = (
        ('indicators', {
            'BradleySiderograph': {
                'class': BradleySiderograph,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_BradleySiderograph'>
            },
            'HilbertDominantCycle': {
                'class': HilbertDominantCycle,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HilbertDominantCycle'>
            }
        }),
        ('weights', {
            'BradleySiderograph': 1.0,
            'HilbertDominantCycle': 1.0
        })
    )
