import backtrader as bt
from ..base_strategy import FlexibleStrategy

class MomentumTrendStrength_MoneyFlowIndex_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von MomentumTrendStrength und MoneyFlowIndex
    """
    
    params = (
        ('indicators', {
            'MomentumTrendStrength': {
                'class': MomentumTrendStrength,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MomentumTrendStrength'>
            },
            'MoneyFlowIndex': {
                'class': MoneyFlowIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MoneyFlowIndex'>
            }
        }),
        ('weights', {
            'MomentumTrendStrength': 1.0,
            'MoneyFlowIndex': 1.0
        })
    )
