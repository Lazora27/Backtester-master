import backtrader as bt
from ..base_strategy import FlexibleStrategy

class StochasticMomentumIndex_HilbertTrendline_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von StochasticMomentumIndex und HilbertTrendline
    """
    
    params = (
        ('indicators', {
            'StochasticMomentumIndex': {
                'class': StochasticMomentumIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_StochasticMomentumIndex'>
            },
            'HilbertTrendline': {
                'class': HilbertTrendline,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HilbertTrendline'>
            }
        }),
        ('weights', {
            'StochasticMomentumIndex': 1.0,
            'HilbertTrendline': 1.0
        })
    )
