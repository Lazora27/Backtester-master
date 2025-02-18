import backtrader as bt
from ..base_strategy import FlexibleStrategy

class HullMovingAverage_StandardDeviationIndicator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von HullMovingAverage und StandardDeviationIndicator
    """
    
    params = (
        ('indicators', {
            'HullMovingAverage': {
                'class': HullMovingAverage,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HullMovingAverage'>
            },
            'StandardDeviationIndicator': {
                'class': StandardDeviationIndicator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_StandardDeviationIndicator'>
            }
        }),
        ('weights', {
            'HullMovingAverage': 1.0,
            'StandardDeviationIndicator': 1.0
        })
    )
