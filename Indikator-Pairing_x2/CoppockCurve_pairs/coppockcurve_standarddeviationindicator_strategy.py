import backtrader as bt
from ..base_strategy import FlexibleStrategy

class CoppockCurve_StandardDeviationIndicator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von CoppockCurve und StandardDeviationIndicator
    """
    
    params = (
        ('indicators', {
            'CoppockCurve': {
                'class': CoppockCurve,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CoppockCurve'>
            },
            'StandardDeviationIndicator': {
                'class': StandardDeviationIndicator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_StandardDeviationIndicator'>
            }
        }),
        ('weights', {
            'CoppockCurve': 1.0,
            'StandardDeviationIndicator': 1.0
        })
    )
