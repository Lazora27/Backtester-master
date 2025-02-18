import backtrader as bt
from ..base_strategy import FlexibleStrategy

class NVISignals_StandardDeviationIndicator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von NVISignals und StandardDeviationIndicator
    """
    
    params = (
        ('indicators', {
            'NVISignals': {
                'class': NVISignals,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_NVISignals'>
            },
            'StandardDeviationIndicator': {
                'class': StandardDeviationIndicator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_StandardDeviationIndicator'>
            }
        }),
        ('weights', {
            'NVISignals': 1.0,
            'StandardDeviationIndicator': 1.0
        })
    )
