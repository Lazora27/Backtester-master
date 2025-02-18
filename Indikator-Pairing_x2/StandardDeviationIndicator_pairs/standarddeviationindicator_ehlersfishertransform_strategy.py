import backtrader as bt
from ..base_strategy import FlexibleStrategy

class StandardDeviationIndicator_EhlersFisherTransform_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von StandardDeviationIndicator und EhlersFisherTransform
    """
    
    params = (
        ('indicators', {
            'StandardDeviationIndicator': {
                'class': StandardDeviationIndicator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_StandardDeviationIndicator'>
            },
            'EhlersFisherTransform': {
                'class': EhlersFisherTransform,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_EhlersFisherTransform'>
            }
        }),
        ('weights', {
            'StandardDeviationIndicator': 1.0,
            'EhlersFisherTransform': 1.0
        })
    )
