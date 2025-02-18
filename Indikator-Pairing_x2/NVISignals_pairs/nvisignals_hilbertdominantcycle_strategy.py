import backtrader as bt
from ..base_strategy import FlexibleStrategy

class NVISignals_HilbertDominantCycle_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von NVISignals und HilbertDominantCycle
    """
    
    params = (
        ('indicators', {
            'NVISignals': {
                'class': NVISignals,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_NVISignals'>
            },
            'HilbertDominantCycle': {
                'class': HilbertDominantCycle,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HilbertDominantCycle'>
            }
        }),
        ('weights', {
            'NVISignals': 1.0,
            'HilbertDominantCycle': 1.0
        })
    )
