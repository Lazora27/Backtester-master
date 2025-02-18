import backtrader as bt
from ..base_strategy import FlexibleStrategy

class MACDDivergence_StochasticRSI_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von MACDDivergence und StochasticRSI
    """
    
    params = (
        ('indicators', {
            'MACDDivergence': {
                'class': MACDDivergence,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MACDDivergence'>
            },
            'StochasticRSI': {
                'class': StochasticRSI,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_StochasticRSI'>
            }
        }),
        ('weights', {
            'MACDDivergence': 1.0,
            'StochasticRSI': 1.0
        })
    )
