import backtrader as bt
from ..base_strategy import FlexibleStrategy

class StandardDeviationIndicator_SmoothedCycle_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von StandardDeviationIndicator und SmoothedCycle
    """
    
    params = (
        ('indicators', {
            'StandardDeviationIndicator': {
                'class': StandardDeviationIndicator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_StandardDeviationIndicator'>
            },
            'SmoothedCycle': {
                'class': SmoothedCycle,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SmoothedCycle'>
            }
        }),
        ('weights', {
            'StandardDeviationIndicator': 1.0,
            'SmoothedCycle': 1.0
        })
    )
