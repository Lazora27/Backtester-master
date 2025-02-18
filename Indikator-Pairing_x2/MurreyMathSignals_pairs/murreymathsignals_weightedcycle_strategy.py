import backtrader as bt
from ..base_strategy import FlexibleStrategy

class MurreyMathSignals_WeightedCycle_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von MurreyMathSignals und WeightedCycle
    """
    
    params = (
        ('indicators', {
            'MurreyMathSignals': {
                'class': MurreyMathSignals,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MurreyMathSignals'>
            },
            'WeightedCycle': {
                'class': WeightedCycle,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_WeightedCycle'>
            }
        }),
        ('weights', {
            'MurreyMathSignals': 1.0,
            'WeightedCycle': 1.0
        })
    )
