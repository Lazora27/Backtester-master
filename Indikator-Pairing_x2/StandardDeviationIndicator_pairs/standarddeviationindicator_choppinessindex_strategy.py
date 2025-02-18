import backtrader as bt
from ..base_strategy import FlexibleStrategy

class StandardDeviationIndicator_ChoppinessIndex_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von StandardDeviationIndicator und ChoppinessIndex
    """
    
    params = (
        ('indicators', {
            'StandardDeviationIndicator': {
                'class': StandardDeviationIndicator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_StandardDeviationIndicator'>
            },
            'ChoppinessIndex': {
                'class': ChoppinessIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ChoppinessIndex'>
            }
        }),
        ('weights', {
            'StandardDeviationIndicator': 1.0,
            'ChoppinessIndex': 1.0
        })
    )
