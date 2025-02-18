import backtrader as bt
from ..base_strategy import FlexibleStrategy

class StochasticRSI_RoundNumbersIndicator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von StochasticRSI und RoundNumbersIndicator
    """
    
    params = (
        ('indicators', {
            'StochasticRSI': {
                'class': StochasticRSI,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_StochasticRSI'>
            },
            'RoundNumbersIndicator': {
                'class': RoundNumbersIndicator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_RoundNumbersIndicator'>
            }
        }),
        ('weights', {
            'StochasticRSI': 1.0,
            'RoundNumbersIndicator': 1.0
        })
    )
