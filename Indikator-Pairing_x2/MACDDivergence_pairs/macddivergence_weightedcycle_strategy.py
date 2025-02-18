import backtrader as bt
from ..base_strategy import FlexibleStrategy

class MACDDivergence_WeightedCycle_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von MACDDivergence und WeightedCycle
    """
    
    params = (
        ('indicators', {
            'MACDDivergence': {
                'class': MACDDivergence,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MACDDivergence'>
            },
            'WeightedCycle': {
                'class': WeightedCycle,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_WeightedCycle'>
            }
        }),
        ('weights', {
            'MACDDivergence': 1.0,
            'WeightedCycle': 1.0
        })
    )
