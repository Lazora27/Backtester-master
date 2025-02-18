import backtrader as bt
from ..base_strategy import FlexibleStrategy

class MoneyFlowIndex_PhaseDivergence_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von MoneyFlowIndex und PhaseDivergence
    """
    
    params = (
        ('indicators', {
            'MoneyFlowIndex': {
                'class': MoneyFlowIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MoneyFlowIndex'>
            },
            'PhaseDivergence': {
                'class': PhaseDivergence,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PhaseDivergence'>
            }
        }),
        ('weights', {
            'MoneyFlowIndex': 1.0,
            'PhaseDivergence': 1.0
        })
    )
