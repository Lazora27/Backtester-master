import backtrader as bt
from ..base_strategy import FlexibleStrategy

class TickVolume_StandardDeviationIndicator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von TickVolume und StandardDeviationIndicator
    """
    
    params = (
        ('indicators', {
            'TickVolume': {
                'class': TickVolume,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TickVolume'>
            },
            'StandardDeviationIndicator': {
                'class': StandardDeviationIndicator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_StandardDeviationIndicator'>
            }
        }),
        ('weights', {
            'TickVolume': 1.0,
            'StandardDeviationIndicator': 1.0
        })
    )
