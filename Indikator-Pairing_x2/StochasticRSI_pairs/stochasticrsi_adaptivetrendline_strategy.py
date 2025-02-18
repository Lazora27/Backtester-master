import backtrader as bt
from ..base_strategy import FlexibleStrategy

class StochasticRSI_AdaptiveTrendLine_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von StochasticRSI und AdaptiveTrendLine
    """
    
    params = (
        ('indicators', {
            'StochasticRSI': {
                'class': StochasticRSI,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_StochasticRSI'>
            },
            'AdaptiveTrendLine': {
                'class': AdaptiveTrendLine,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AdaptiveTrendLine'>
            }
        }),
        ('weights', {
            'StochasticRSI': 1.0,
            'AdaptiveTrendLine': 1.0
        })
    )
