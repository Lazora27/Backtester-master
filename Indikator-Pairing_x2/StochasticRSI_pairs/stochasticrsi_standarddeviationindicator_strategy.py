import backtrader as bt
from ..base_strategy import FlexibleStrategy

class StochasticRSI_StandardDeviationIndicator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von StochasticRSI und StandardDeviationIndicator
    """
    
    params = (
        ('indicators', {
            'StochasticRSI': {
                'class': StochasticRSI,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_StochasticRSI'>
            },
            'StandardDeviationIndicator': {
                'class': StandardDeviationIndicator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_StandardDeviationIndicator'>
            }
        }),
        ('weights', {
            'StochasticRSI': 1.0,
            'StandardDeviationIndicator': 1.0
        })
    )
