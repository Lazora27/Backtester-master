import backtrader as bt
from ..base_strategy import FlexibleStrategy

class MovingAverageCycleDetector_ParabolicTimePrice_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von MovingAverageCycleDetector und ParabolicTimePrice
    """
    
    params = (
        ('indicators', {
            'MovingAverageCycleDetector': {
                'class': MovingAverageCycleDetector,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MovingAverageCycleDetector'>
            },
            'ParabolicTimePrice': {
                'class': ParabolicTimePrice,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ParabolicTimePrice'>
            }
        }),
        ('weights', {
            'MovingAverageCycleDetector': 1.0,
            'ParabolicTimePrice': 1.0
        })
    )
