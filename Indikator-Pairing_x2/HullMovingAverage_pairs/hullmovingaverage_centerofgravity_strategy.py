import backtrader as bt
from ..base_strategy import FlexibleStrategy

class HullMovingAverage_CenterOfGravity_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von HullMovingAverage und CenterOfGravity
    """
    
    params = (
        ('indicators', {
            'HullMovingAverage': {
                'class': HullMovingAverage,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HullMovingAverage'>
            },
            'CenterOfGravity': {
                'class': CenterOfGravity,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CenterOfGravity'>
            }
        }),
        ('weights', {
            'HullMovingAverage': 1.0,
            'CenterOfGravity': 1.0
        })
    )
