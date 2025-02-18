import backtrader as bt
from ..base_strategy import FlexibleStrategy

class GannAngles_StandardDeviationIndicator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von GannAngles und StandardDeviationIndicator
    """
    
    params = (
        ('indicators', {
            'GannAngles': {
                'class': GannAngles,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_GannAngles1'>
            },
            'StandardDeviationIndicator': {
                'class': StandardDeviationIndicator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_StandardDeviationIndicator'>
            }
        }),
        ('weights', {
            'GannAngles': 1.0,
            'StandardDeviationIndicator': 1.0
        })
    )
