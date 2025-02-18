import backtrader as bt
from ..base_strategy import FlexibleStrategy

class MomentumIndicator_WeightedCycle_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von MomentumIndicator und WeightedCycle
    """
    
    params = (
        ('indicators', {
            'MomentumIndicator': {
                'class': MomentumIndicator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MomentumIndicator'>
            },
            'WeightedCycle': {
                'class': WeightedCycle,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_WeightedCycle'>
            }
        }),
        ('weights', {
            'MomentumIndicator': 1.0,
            'WeightedCycle': 1.0
        })
    )
