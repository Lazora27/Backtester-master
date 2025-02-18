import backtrader as bt
from ..base_strategy import FlexibleStrategy

class StochasticRSI_DOMDepth_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von StochasticRSI und DOMDepth
    """
    
    params = (
        ('indicators', {
            'StochasticRSI': {
                'class': StochasticRSI,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_StochasticRSI'>
            },
            'DOMDepth': {
                'class': DOMDepth,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_DOMDepth'>
            }
        }),
        ('weights', {
            'StochasticRSI': 1.0,
            'DOMDepth': 1.0
        })
    )
