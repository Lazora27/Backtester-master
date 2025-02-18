import backtrader as bt
from ..base_strategy import FlexibleStrategy

class FlowOfFunds_AccumulationDistributionLine_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von FlowOfFunds und AccumulationDistributionLine
    """
    
    params = (
        ('indicators', {
            'FlowOfFunds': {
                'class': FlowOfFunds,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FlowOfFunds'>
            },
            'AccumulationDistributionLine': {
                'class': AccumulationDistributionLine,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AccumulationDistributionLine'>
            }
        }),
        ('weights', {
            'FlowOfFunds': 1.0,
            'AccumulationDistributionLine': 1.0
        })
    )
