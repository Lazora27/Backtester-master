import backtrader as bt
from ..base_strategy import FlexibleStrategy

class CCITurbo_HilbertDominantCycle_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von CCITurbo und HilbertDominantCycle
    """
    
    params = (
        ('indicators', {
            'CCITurbo': {
                'class': CCITurbo,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CCITurbo'>
            },
            'HilbertDominantCycle': {
                'class': HilbertDominantCycle,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HilbertDominantCycle'>
            }
        }),
        ('weights', {
            'CCITurbo': 1.0,
            'HilbertDominantCycle': 1.0
        })
    )
