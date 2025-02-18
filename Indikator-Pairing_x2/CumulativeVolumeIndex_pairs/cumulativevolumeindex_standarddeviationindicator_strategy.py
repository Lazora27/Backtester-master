import backtrader as bt
from ..base_strategy import FlexibleStrategy

class CumulativeVolumeIndex_StandardDeviationIndicator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von CumulativeVolumeIndex und StandardDeviationIndicator
    """
    
    params = (
        ('indicators', {
            'CumulativeVolumeIndex': {
                'class': CumulativeVolumeIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CumulativeVolumeIndex'>
            },
            'StandardDeviationIndicator': {
                'class': StandardDeviationIndicator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_StandardDeviationIndicator'>
            }
        }),
        ('weights', {
            'CumulativeVolumeIndex': 1.0,
            'StandardDeviationIndicator': 1.0
        })
    )
