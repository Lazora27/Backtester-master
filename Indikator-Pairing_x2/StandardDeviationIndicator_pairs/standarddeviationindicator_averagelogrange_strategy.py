import backtrader as bt
from ..base_strategy import FlexibleStrategy

class StandardDeviationIndicator_AverageLogRange_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von StandardDeviationIndicator und AverageLogRange
    """
    
    params = (
        ('indicators', {
            'StandardDeviationIndicator': {
                'class': StandardDeviationIndicator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_StandardDeviationIndicator'>
            },
            'AverageLogRange': {
                'class': AverageLogRange,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AverageLogRange'>
            }
        }),
        ('weights', {
            'StandardDeviationIndicator': 1.0,
            'AverageLogRange': 1.0
        })
    )
