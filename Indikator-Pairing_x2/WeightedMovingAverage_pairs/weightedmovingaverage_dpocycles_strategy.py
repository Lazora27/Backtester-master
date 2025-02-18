import backtrader as bt
from ..base_strategy import FlexibleStrategy

class WeightedMovingAverage_DPOCycles_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von WeightedMovingAverage und DPOCycles
    """
    
    params = (
        ('indicators', {
            'WeightedMovingAverage': {
                'class': WeightedMovingAverage,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_WeightedMovingAverage'>
            },
            'DPOCycles': {
                'class': DPOCycles,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_DPOCycles'>
            }
        }),
        ('weights', {
            'WeightedMovingAverage': 1.0,
            'DPOCycles': 1.0
        })
    )
