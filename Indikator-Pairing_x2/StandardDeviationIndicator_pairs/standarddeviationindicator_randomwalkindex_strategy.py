import backtrader as bt
from ..base_strategy import FlexibleStrategy

class StandardDeviationIndicator_RandomWalkIndex_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von StandardDeviationIndicator und RandomWalkIndex
    """
    
    params = (
        ('indicators', {
            'StandardDeviationIndicator': {
                'class': StandardDeviationIndicator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_StandardDeviationIndicator'>
            },
            'RandomWalkIndex': {
                'class': RandomWalkIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_RandomWalkIndex'>
            }
        }),
        ('weights', {
            'StandardDeviationIndicator': 1.0,
            'RandomWalkIndex': 1.0
        })
    )
