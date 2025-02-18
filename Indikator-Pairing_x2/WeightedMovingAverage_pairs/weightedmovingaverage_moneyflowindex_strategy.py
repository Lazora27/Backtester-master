import backtrader as bt
from ..base_strategy import FlexibleStrategy

class WeightedMovingAverage_MoneyFlowIndex_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von WeightedMovingAverage und MoneyFlowIndex
    """
    
    params = (
        ('indicators', {
            'WeightedMovingAverage': {
                'class': WeightedMovingAverage,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_WeightedMovingAverage'>
            },
            'MoneyFlowIndex': {
                'class': MoneyFlowIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MoneyFlowIndex'>
            }
        }),
        ('weights', {
            'WeightedMovingAverage': 1.0,
            'MoneyFlowIndex': 1.0
        })
    )
