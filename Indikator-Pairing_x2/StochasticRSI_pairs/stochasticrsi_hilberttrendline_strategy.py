import backtrader as bt
from ..base_strategy import FlexibleStrategy

class StochasticRSI_HilbertTrendline_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von StochasticRSI und HilbertTrendline
    """
    
    params = (
        ('indicators', {
            'StochasticRSI': {
                'class': StochasticRSI,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_StochasticRSI'>
            },
            'HilbertTrendline': {
                'class': HilbertTrendline,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HilbertTrendline'>
            }
        }),
        ('weights', {
            'StochasticRSI': 1.0,
            'HilbertTrendline': 1.0
        })
    )
