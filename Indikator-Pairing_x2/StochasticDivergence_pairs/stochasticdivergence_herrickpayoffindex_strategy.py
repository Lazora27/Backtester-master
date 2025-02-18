import backtrader as bt
from ..base_strategy import FlexibleStrategy

class StochasticDivergence_HerrickPayoffIndex_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von StochasticDivergence und HerrickPayoffIndex
    """
    
    params = (
        ('indicators', {
            'StochasticDivergence': {
                'class': StochasticDivergence,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_StochasticDivergence'>
            },
            'HerrickPayoffIndex': {
                'class': HerrickPayoffIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HerrickPayoffIndex'>
            }
        }),
        ('weights', {
            'StochasticDivergence': 1.0,
            'HerrickPayoffIndex': 1.0
        })
    )
