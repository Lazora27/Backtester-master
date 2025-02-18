import backtrader as bt
from ..base_strategy import FlexibleStrategy

class StochasticDivergence_VWAPDeviationBands_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von StochasticDivergence und VWAPDeviationBands
    """
    
    params = (
        ('indicators', {
            'StochasticDivergence': {
                'class': StochasticDivergence,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_StochasticDivergence'>
            },
            'VWAPDeviationBands': {
                'class': VWAPDeviationBands,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_VWAPDeviationBands'>
            }
        }),
        ('weights', {
            'StochasticDivergence': 1.0,
            'VWAPDeviationBands': 1.0
        })
    )
