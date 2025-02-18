import backtrader as bt
from ..base_strategy import FlexibleStrategy

class AccumulationDistributionLine_SmoothedCycle_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von AccumulationDistributionLine und SmoothedCycle
    """
    
    params = (
        ('indicators', {
            'AccumulationDistributionLine': {
                'class': AccumulationDistributionLine,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AccumulationDistributionLine'>
            },
            'SmoothedCycle': {
                'class': SmoothedCycle,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SmoothedCycle'>
            }
        }),
        ('weights', {
            'AccumulationDistributionLine': 1.0,
            'SmoothedCycle': 1.0
        })
    )
