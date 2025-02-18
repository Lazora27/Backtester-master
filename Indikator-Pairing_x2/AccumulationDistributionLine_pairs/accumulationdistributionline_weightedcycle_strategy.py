import backtrader as bt
from ..base_strategy import FlexibleStrategy

class AccumulationDistributionLine_WeightedCycle_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von AccumulationDistributionLine und WeightedCycle
    """
    
    params = (
        ('indicators', {
            'AccumulationDistributionLine': {
                'class': AccumulationDistributionLine,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AccumulationDistributionLine'>
            },
            'WeightedCycle': {
                'class': WeightedCycle,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_WeightedCycle'>
            }
        }),
        ('weights', {
            'AccumulationDistributionLine': 1.0,
            'WeightedCycle': 1.0
        })
    )
