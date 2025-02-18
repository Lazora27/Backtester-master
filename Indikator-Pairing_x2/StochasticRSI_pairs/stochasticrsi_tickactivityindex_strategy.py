import backtrader as bt
from ..base_strategy import FlexibleStrategy

class StochasticRSI_TickActivityIndex_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von StochasticRSI und TickActivityIndex
    """
    
    params = (
        ('indicators', {
            'StochasticRSI': {
                'class': StochasticRSI,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_StochasticRSI'>
            },
            'TickActivityIndex': {
                'class': TickActivityIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TickActivityIndex'>
            }
        }),
        ('weights', {
            'StochasticRSI': 1.0,
            'TickActivityIndex': 1.0
        })
    )
