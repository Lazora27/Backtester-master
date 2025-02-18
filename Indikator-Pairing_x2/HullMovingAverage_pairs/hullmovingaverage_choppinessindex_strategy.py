import backtrader as bt
from ..base_strategy import FlexibleStrategy

class HullMovingAverage_ChoppinessIndex_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von HullMovingAverage und ChoppinessIndex
    """
    
    params = (
        ('indicators', {
            'HullMovingAverage': {
                'class': HullMovingAverage,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HullMovingAverage'>
            },
            'ChoppinessIndex': {
                'class': ChoppinessIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ChoppinessIndex'>
            }
        }),
        ('weights', {
            'HullMovingAverage': 1.0,
            'ChoppinessIndex': 1.0
        })
    )
