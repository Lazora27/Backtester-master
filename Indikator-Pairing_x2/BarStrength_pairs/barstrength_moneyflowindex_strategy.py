import backtrader as bt
from ..base_strategy import FlexibleStrategy

class BarStrength_MoneyFlowIndex_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von BarStrength und MoneyFlowIndex
    """
    
    params = (
        ('indicators', {
            'BarStrength': {
                'class': BarStrength,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_BarStrength'>
            },
            'MoneyFlowIndex': {
                'class': MoneyFlowIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MoneyFlowIndex'>
            }
        }),
        ('weights', {
            'BarStrength': 1.0,
            'MoneyFlowIndex': 1.0
        })
    )
