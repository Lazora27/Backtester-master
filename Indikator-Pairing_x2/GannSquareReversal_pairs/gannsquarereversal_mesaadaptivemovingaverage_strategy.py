import backtrader as bt
from ..base_strategy import FlexibleStrategy

class GannSquareReversal_MESAAdaptiveMovingAverage_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von GannSquareReversal und MESAAdaptiveMovingAverage
    """
    
    params = (
        ('indicators', {
            'GannSquareReversal': {
                'class': GannSquareReversal,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_GannSquareReversal'>
            },
            'MESAAdaptiveMovingAverage': {
                'class': MESAAdaptiveMovingAverage,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MESAAdaptiveMovingAverage'>
            }
        }),
        ('weights', {
            'GannSquareReversal': 1.0,
            'MESAAdaptiveMovingAverage': 1.0
        })
    )
