import backtrader as bt
from ..base_strategy import FlexibleStrategy

class DeltaProfile_StandardDeviationIndicator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von DeltaProfile und StandardDeviationIndicator
    """
    
    params = (
        ('indicators', {
            'DeltaProfile': {
                'class': DeltaProfile,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_DeltaProfile'>
            },
            'StandardDeviationIndicator': {
                'class': StandardDeviationIndicator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_StandardDeviationIndicator'>
            }
        }),
        ('weights', {
            'DeltaProfile': 1.0,
            'StandardDeviationIndicator': 1.0
        })
    )
