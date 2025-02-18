import backtrader as bt
from ..base_strategy import FlexibleStrategy

class WilliamsR_StandardDeviationIndicator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von WilliamsR und StandardDeviationIndicator
    """
    
    params = (
        ('indicators', {
            'WilliamsR': {
                'class': WilliamsR,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_WilliamsR1'>
            },
            'StandardDeviationIndicator': {
                'class': StandardDeviationIndicator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_StandardDeviationIndicator'>
            }
        }),
        ('weights', {
            'WilliamsR': 1.0,
            'StandardDeviationIndicator': 1.0
        })
    )
