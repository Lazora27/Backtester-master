import backtrader as bt
from ..base_strategy import FlexibleStrategy

class HilbertTrendSignals_WeightedCycle_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von HilbertTrendSignals und WeightedCycle
    """
    
    params = (
        ('indicators', {
            'HilbertTrendSignals': {
                'class': HilbertTrendSignals,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HilbertTrendSignals'>
            },
            'WeightedCycle': {
                'class': WeightedCycle,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_WeightedCycle'>
            }
        }),
        ('weights', {
            'HilbertTrendSignals': 1.0,
            'WeightedCycle': 1.0
        })
    )
