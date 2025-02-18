import backtrader as bt
from ..base_strategy import FlexibleStrategy

class PVINVIComparison_StandardDeviationIndicator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von PVINVIComparison und StandardDeviationIndicator
    """
    
    params = (
        ('indicators', {
            'PVINVIComparison': {
                'class': PVINVIComparison,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PVINVIComparison'>
            },
            'StandardDeviationIndicator': {
                'class': StandardDeviationIndicator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_StandardDeviationIndicator'>
            }
        }),
        ('weights', {
            'PVINVIComparison': 1.0,
            'StandardDeviationIndicator': 1.0
        })
    )
