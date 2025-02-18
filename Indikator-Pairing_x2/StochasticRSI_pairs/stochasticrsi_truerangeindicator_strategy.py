import backtrader as bt
from ..base_strategy import FlexibleStrategy

class StochasticRSI_TrueRangeIndicator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von StochasticRSI und TrueRangeIndicator
    """
    
    params = (
        ('indicators', {
            'StochasticRSI': {
                'class': StochasticRSI,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_StochasticRSI'>
            },
            'TrueRangeIndicator': {
                'class': TrueRangeIndicator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TrueRangeIndicator'>
            }
        }),
        ('weights', {
            'StochasticRSI': 1.0,
            'TrueRangeIndicator': 1.0
        })
    )
