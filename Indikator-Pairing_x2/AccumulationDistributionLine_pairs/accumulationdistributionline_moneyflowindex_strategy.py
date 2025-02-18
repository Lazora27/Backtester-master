import backtrader as bt
from ..base_strategy import FlexibleStrategy

class AccumulationDistributionLine_MoneyFlowIndex_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von AccumulationDistributionLine und MoneyFlowIndex
    """
    
    params = (
        ('indicators', {
            'AccumulationDistributionLine': {
                'class': AccumulationDistributionLine,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AccumulationDistributionLine'>
            },
            'MoneyFlowIndex': {
                'class': MoneyFlowIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MoneyFlowIndex'>
            }
        }),
        ('weights', {
            'AccumulationDistributionLine': 1.0,
            'MoneyFlowIndex': 1.0
        })
    )
