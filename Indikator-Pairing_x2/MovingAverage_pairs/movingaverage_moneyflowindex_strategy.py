import backtrader as bt
from ..base_strategy import FlexibleStrategy

class MovingAverage_MoneyFlowIndex_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von MovingAverage und MoneyFlowIndex
    """
    
    params = (
        ('indicators', {
            'MovingAverage': {
                'class': MovingAverage,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MovingAverage'>
            },
            'MoneyFlowIndex': {
                'class': MoneyFlowIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MoneyFlowIndex'>
            }
        }),
        ('weights', {
            'MovingAverage': 1.0,
            'MoneyFlowIndex': 1.0
        })
    )
