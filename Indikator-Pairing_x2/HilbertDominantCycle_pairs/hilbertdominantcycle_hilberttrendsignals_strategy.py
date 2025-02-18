import backtrader as bt
from ..base_strategy import FlexibleStrategy

class HilbertDominantCycle_HilbertTrendSignals_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von HilbertDominantCycle und HilbertTrendSignals
    """
    
    params = (
        ('indicators', {
            'HilbertDominantCycle': {
                'class': HilbertDominantCycle,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HilbertDominantCycle'>
            },
            'HilbertTrendSignals': {
                'class': HilbertTrendSignals,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HilbertTrendSignals'>
            }
        }),
        ('weights', {
            'HilbertDominantCycle': 1.0,
            'HilbertTrendSignals': 1.0
        })
    )
