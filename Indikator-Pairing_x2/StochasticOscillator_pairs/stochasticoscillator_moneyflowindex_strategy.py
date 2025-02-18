import backtrader as bt
from ..base_strategy import FlexibleStrategy

class StochasticOscillator_MoneyFlowIndex_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von StochasticOscillator und MoneyFlowIndex
    """
    
    params = (
        ('indicators', {
            'StochasticOscillator': {
                'class': StochasticOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_StochasticOscillator'>
            },
            'MoneyFlowIndex': {
                'class': MoneyFlowIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MoneyFlowIndex'>
            }
        }),
        ('weights', {
            'StochasticOscillator': 1.0,
            'MoneyFlowIndex': 1.0
        })
    )
