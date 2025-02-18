import backtrader as bt
from ..base_strategy import FlexibleStrategy

class VolumeProfile_StandardDeviationIndicator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von VolumeProfile und StandardDeviationIndicator
    """
    
    params = (
        ('indicators', {
            'VolumeProfile': {
                'class': VolumeProfile,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_VolumeProfile'>
            },
            'StandardDeviationIndicator': {
                'class': StandardDeviationIndicator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_StandardDeviationIndicator'>
            }
        }),
        ('weights', {
            'VolumeProfile': 1.0,
            'StandardDeviationIndicator': 1.0
        })
    )
