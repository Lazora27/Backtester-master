import backtrader as bt
from ..base_strategy import FlexibleStrategy

class FisherTransform_StandardDeviationIndicator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von FisherTransform und StandardDeviationIndicator
    """
    
    params = (
        ('indicators', {
            'FisherTransform': {
                'class': FisherTransform,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FisherTransform'>
            },
            'StandardDeviationIndicator': {
                'class': StandardDeviationIndicator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_StandardDeviationIndicator'>
            }
        }),
        ('weights', {
            'FisherTransform': 1.0,
            'StandardDeviationIndicator': 1.0
        })
    )
