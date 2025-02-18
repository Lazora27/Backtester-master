import backtrader as bt
from ..base_strategy import FlexibleStrategy

class MoneyFlowIndex_TrendCycles_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von MoneyFlowIndex und TrendCycles
    """
    
    params = (
        ('indicators', {
            'MoneyFlowIndex': {
                'class': MoneyFlowIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MoneyFlowIndex'>
            },
            'TrendCycles': {
                'class': TrendCycles,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TrendCycles'>
            }
        }),
        ('weights', {
            'MoneyFlowIndex': 1.0,
            'TrendCycles': 1.0
        })
    )
