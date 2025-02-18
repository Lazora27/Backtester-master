import backtrader as bt
from ..base_strategy import FlexibleStrategy

class StochasticDivergence_VWAPBands_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von StochasticDivergence und VWAPBands
    """
    
    params = (
        ('indicators', {
            'StochasticDivergence': {
                'class': StochasticDivergence,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_StochasticDivergence'>
            },
            'VWAPBands': {
                'class': VWAPBands,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_VWAPBands'>
            }
        }),
        ('weights', {
            'StochasticDivergence': 1.0,
            'VWAPBands': 1.0
        })
    )
