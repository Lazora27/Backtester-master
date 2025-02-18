import backtrader as bt
from ..base_strategy import FlexibleStrategy

class StochasticDivergence_CVIRatio_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von StochasticDivergence und CVIRatio
    """
    
    params = (
        ('indicators', {
            'StochasticDivergence': {
                'class': StochasticDivergence,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_StochasticDivergence'>
            },
            'CVIRatio': {
                'class': CVIRatio,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CVIRatio'>
            }
        }),
        ('weights', {
            'StochasticDivergence': 1.0,
            'CVIRatio': 1.0
        })
    )
