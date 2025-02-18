import backtrader as bt
from ..base_strategy import FlexibleStrategy

class CVIRatio_StandardDeviationIndicator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von CVIRatio und StandardDeviationIndicator
    """
    
    params = (
        ('indicators', {
            'CVIRatio': {
                'class': CVIRatio,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CVIRatio'>
            },
            'StandardDeviationIndicator': {
                'class': StandardDeviationIndicator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_StandardDeviationIndicator'>
            }
        }),
        ('weights', {
            'CVIRatio': 1.0,
            'StandardDeviationIndicator': 1.0
        })
    )
