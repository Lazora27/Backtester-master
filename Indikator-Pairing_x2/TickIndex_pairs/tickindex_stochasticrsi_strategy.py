import backtrader as bt
from ..base_strategy import FlexibleStrategy

class TickIndex_StochasticRSI_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von TickIndex und StochasticRSI
    """
    
    params = (
        ('indicators', {
            'TickIndex': {
                'class': TickIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TickIndex'>
            },
            'StochasticRSI': {
                'class': StochasticRSI,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_StochasticRSI'>
            }
        }),
        ('weights', {
            'TickIndex': 1.0,
            'StochasticRSI': 1.0
        })
    )
