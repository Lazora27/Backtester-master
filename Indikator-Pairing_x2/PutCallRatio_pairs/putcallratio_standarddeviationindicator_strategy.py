import backtrader as bt
from ..base_strategy import FlexibleStrategy

class PutCallRatio_StandardDeviationIndicator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von PutCallRatio und StandardDeviationIndicator
    """
    
    params = (
        ('indicators', {
            'PutCallRatio': {
                'class': PutCallRatio,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PutCallRatio1'>
            },
            'StandardDeviationIndicator': {
                'class': StandardDeviationIndicator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_StandardDeviationIndicator'>
            }
        }),
        ('weights', {
            'PutCallRatio': 1.0,
            'StandardDeviationIndicator': 1.0
        })
    )
