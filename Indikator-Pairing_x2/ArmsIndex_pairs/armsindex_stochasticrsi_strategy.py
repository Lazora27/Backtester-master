import backtrader as bt
from ..base_strategy import FlexibleStrategy

class ArmsIndex_StochasticRSI_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von ArmsIndex und StochasticRSI
    """
    
    params = (
        ('indicators', {
            'ArmsIndex': {
                'class': ArmsIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ArmsIndex'>
            },
            'StochasticRSI': {
                'class': StochasticRSI,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_StochasticRSI'>
            }
        }),
        ('weights', {
            'ArmsIndex': 1.0,
            'StochasticRSI': 1.0
        })
    )
