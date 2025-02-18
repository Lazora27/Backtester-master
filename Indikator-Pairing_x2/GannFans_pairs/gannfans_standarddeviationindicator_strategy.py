import backtrader as bt
from ..base_strategy import FlexibleStrategy

class GannFans_StandardDeviationIndicator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von GannFans und StandardDeviationIndicator
    """
    
    params = (
        ('indicators', {
            'GannFans': {
                'class': GannFans,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_GannFans'>
            },
            'StandardDeviationIndicator': {
                'class': StandardDeviationIndicator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_StandardDeviationIndicator'>
            }
        }),
        ('weights', {
            'GannFans': 1.0,
            'StandardDeviationIndicator': 1.0
        })
    )
