import backtrader as bt
from ..base_strategy import FlexibleStrategy

class StochasticRSI_UlcerIndex_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von StochasticRSI und UlcerIndex
    """
    
    params = (
        ('indicators', {
            'StochasticRSI': {
                'class': StochasticRSI,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_StochasticRSI'>
            },
            'UlcerIndex': {
                'class': UlcerIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_UlcerIndex'>
            }
        }),
        ('weights', {
            'StochasticRSI': 1.0,
            'UlcerIndex': 1.0
        })
    )
