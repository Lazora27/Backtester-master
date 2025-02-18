import backtrader as bt
from ..base_strategy import FlexibleStrategy

class KaufmanEfficiencyRatio_MoneyFlowIndex_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von KaufmanEfficiencyRatio und MoneyFlowIndex
    """
    
    params = (
        ('indicators', {
            'KaufmanEfficiencyRatio': {
                'class': KaufmanEfficiencyRatio,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_KaufmanEfficiencyRatio'>
            },
            'MoneyFlowIndex': {
                'class': MoneyFlowIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MoneyFlowIndex'>
            }
        }),
        ('weights', {
            'KaufmanEfficiencyRatio': 1.0,
            'MoneyFlowIndex': 1.0
        })
    )
