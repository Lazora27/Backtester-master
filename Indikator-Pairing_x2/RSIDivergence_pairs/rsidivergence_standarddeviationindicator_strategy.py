import backtrader as bt
from ..base_strategy import FlexibleStrategy

class RSIDivergence_StandardDeviationIndicator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von RSIDivergence und StandardDeviationIndicator
    """
    
    params = (
        ('indicators', {
            'RSIDivergence': {
                'class': RSIDivergence,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_RSIDivergence'>
            },
            'StandardDeviationIndicator': {
                'class': StandardDeviationIndicator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_StandardDeviationIndicator'>
            }
        }),
        ('weights', {
            'RSIDivergence': 1.0,
            'StandardDeviationIndicator': 1.0
        })
    )
