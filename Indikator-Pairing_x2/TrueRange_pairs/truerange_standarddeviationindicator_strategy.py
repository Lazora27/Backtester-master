import backtrader as bt
from ..base_strategy import FlexibleStrategy

class TrueRange_StandardDeviationIndicator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von TrueRange und StandardDeviationIndicator
    """
    
    params = (
        ('indicators', {
            'TrueRange': {
                'class': TrueRange,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TrueRange1'>
            },
            'StandardDeviationIndicator': {
                'class': StandardDeviationIndicator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_StandardDeviationIndicator'>
            }
        }),
        ('weights', {
            'TrueRange': 1.0,
            'StandardDeviationIndicator': 1.0
        })
    )
