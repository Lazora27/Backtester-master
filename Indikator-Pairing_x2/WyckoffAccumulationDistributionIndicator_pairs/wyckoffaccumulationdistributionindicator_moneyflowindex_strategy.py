import backtrader as bt
from ..base_strategy import FlexibleStrategy

class WyckoffAccumulationDistributionIndicator_MoneyFlowIndex_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von WyckoffAccumulationDistributionIndicator und MoneyFlowIndex
    """
    
    params = (
        ('indicators', {
            'WyckoffAccumulationDistributionIndicator': {
                'class': WyckoffAccumulationDistributionIndicator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_WyckoffAccumulationDistributionIndicator'>
            },
            'MoneyFlowIndex': {
                'class': MoneyFlowIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MoneyFlowIndex'>
            }
        }),
        ('weights', {
            'WyckoffAccumulationDistributionIndicator': 1.0,
            'MoneyFlowIndex': 1.0
        })
    )
