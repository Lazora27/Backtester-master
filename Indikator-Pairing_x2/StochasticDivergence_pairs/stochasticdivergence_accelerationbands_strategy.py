import backtrader as bt
from ..base_strategy import FlexibleStrategy

class StochasticDivergence_AccelerationBands_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von StochasticDivergence und AccelerationBands
    """
    
    params = (
        ('indicators', {
            'StochasticDivergence': {
                'class': StochasticDivergence,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_StochasticDivergence'>
            },
            'AccelerationBands': {
                'class': AccelerationBands,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AccelerationBands'>
            }
        }),
        ('weights', {
            'StochasticDivergence': 1.0,
            'AccelerationBands': 1.0
        })
    )
