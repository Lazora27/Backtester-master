import backtrader as bt
from ..base_strategy import FlexibleStrategy

class CyberCycle_HilbertDominantCycle_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von CyberCycle und HilbertDominantCycle
    """
    
    params = (
        ('indicators', {
            'CyberCycle': {
                'class': CyberCycle,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CyberCycle'>
            },
            'HilbertDominantCycle': {
                'class': HilbertDominantCycle,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HilbertDominantCycle'>
            }
        }),
        ('weights', {
            'CyberCycle': 1.0,
            'HilbertDominantCycle': 1.0
        })
    )
