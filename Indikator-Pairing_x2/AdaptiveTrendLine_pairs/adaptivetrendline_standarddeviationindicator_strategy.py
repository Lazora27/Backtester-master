import backtrader as bt
from ..base_strategy import FlexibleStrategy

class AdaptiveTrendLine_StandardDeviationIndicator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von AdaptiveTrendLine und StandardDeviationIndicator
    """
    
    params = (
        ('indicators', {
            'AdaptiveTrendLine': {
                'class': AdaptiveTrendLine,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AdaptiveTrendLine'>
            },
            'StandardDeviationIndicator': {
                'class': StandardDeviationIndicator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_StandardDeviationIndicator'>
            }
        }),
        ('weights', {
            'AdaptiveTrendLine': 1.0,
            'StandardDeviationIndicator': 1.0
        })
    )
