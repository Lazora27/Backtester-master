import backtrader as bt
from ..base_strategy import FlexibleStrategy

class HullMovingAverage_MoneyFlowIndex_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von HullMovingAverage und MoneyFlowIndex
    """
    
    params = (
        ('indicators', {
            'HullMovingAverage': {
                'class': HullMovingAverage,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HullMovingAverage'>
            },
            'MoneyFlowIndex': {
                'class': MoneyFlowIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MoneyFlowIndex'>
            }
        }),
        ('weights', {
            'HullMovingAverage': 1.0,
            'MoneyFlowIndex': 1.0
        })
    )
