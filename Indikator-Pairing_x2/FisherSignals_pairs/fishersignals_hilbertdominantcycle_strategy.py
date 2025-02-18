import backtrader as bt
from ..base_strategy import FlexibleStrategy

class FisherSignals_HilbertDominantCycle_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von FisherSignals und HilbertDominantCycle
    """
    
    params = (
        ('indicators', {
            'FisherSignals': {
                'class': FisherSignals,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FisherSignals'>
            },
            'HilbertDominantCycle': {
                'class': HilbertDominantCycle,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HilbertDominantCycle'>
            }
        }),
        ('weights', {
            'FisherSignals': 1.0,
            'HilbertDominantCycle': 1.0
        })
    )
