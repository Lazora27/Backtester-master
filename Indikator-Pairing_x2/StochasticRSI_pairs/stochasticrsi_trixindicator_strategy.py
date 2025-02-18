import backtrader as bt
from ..base_strategy import FlexibleStrategy

class StochasticRSI_TRIXIndicator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von StochasticRSI und TRIXIndicator
    """
    
    params = (
        ('indicators', {
            'StochasticRSI': {
                'class': StochasticRSI,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_StochasticRSI'>
            },
            'TRIXIndicator': {
                'class': TRIXIndicator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TRIXIndicator'>
            }
        }),
        ('weights', {
            'StochasticRSI': 1.0,
            'TRIXIndicator': 1.0
        })
    )
