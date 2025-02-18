import backtrader as bt
from ..base_strategy import FlexibleStrategy

class RelativeMomentumIndex_MoneyFlowIndex_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von RelativeMomentumIndex und MoneyFlowIndex
    """
    
    params = (
        ('indicators', {
            'RelativeMomentumIndex': {
                'class': RelativeMomentumIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_RelativeMomentumIndex'>
            },
            'MoneyFlowIndex': {
                'class': MoneyFlowIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MoneyFlowIndex'>
            }
        }),
        ('weights', {
            'RelativeMomentumIndex': 1.0,
            'MoneyFlowIndex': 1.0
        })
    )
