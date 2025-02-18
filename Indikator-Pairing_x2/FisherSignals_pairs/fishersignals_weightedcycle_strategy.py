import backtrader as bt
from ..base_strategy import FlexibleStrategy

class FisherSignals_WeightedCycle_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von FisherSignals und WeightedCycle
    """
    
    params = (
        ('indicators', {
            'FisherSignals': {
                'class': FisherSignals,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FisherSignals'>
            },
            'WeightedCycle': {
                'class': WeightedCycle,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_WeightedCycle'>
            }
        }),
        ('weights', {
            'FisherSignals': 1.0,
            'WeightedCycle': 1.0
        })
    )
