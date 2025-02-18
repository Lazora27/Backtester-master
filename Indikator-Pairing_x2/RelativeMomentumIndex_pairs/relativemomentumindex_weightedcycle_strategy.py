import backtrader as bt
from ..base_strategy import FlexibleStrategy

class RelativeMomentumIndex_WeightedCycle_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von RelativeMomentumIndex und WeightedCycle
    """
    
    params = (
        ('indicators', {
            'RelativeMomentumIndex': {
                'class': RelativeMomentumIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_RelativeMomentumIndex'>
            },
            'WeightedCycle': {
                'class': WeightedCycle,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_WeightedCycle'>
            }
        }),
        ('weights', {
            'RelativeMomentumIndex': 1.0,
            'WeightedCycle': 1.0
        })
    )
