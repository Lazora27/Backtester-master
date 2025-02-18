import backtrader as bt
from ..base_strategy import FlexibleStrategy

class MACDDivergence_StochasticDivergence_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von MACDDivergence und StochasticDivergence
    """
    
    params = (
        ('indicators', {
            'MACDDivergence': {
                'class': MACDDivergence,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MACDDivergence'>
            },
            'StochasticDivergence': {
                'class': StochasticDivergence,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_StochasticDivergence'>
            }
        }),
        ('weights', {
            'MACDDivergence': 1.0,
            'StochasticDivergence': 1.0
        })
    )
