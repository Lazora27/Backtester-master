import backtrader as bt
from ..base_strategy import FlexibleStrategy

class StochasticRSI_TrueRange_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von StochasticRSI und TrueRange
    """
    
    params = (
        ('indicators', {
            'StochasticRSI': {
                'class': StochasticRSI,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_StochasticRSI'>
            },
            'TrueRange': {
                'class': TrueRange,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TrueRange1'>
            }
        }),
        ('weights', {
            'StochasticRSI': 1.0,
            'TrueRange': 1.0
        })
    )
