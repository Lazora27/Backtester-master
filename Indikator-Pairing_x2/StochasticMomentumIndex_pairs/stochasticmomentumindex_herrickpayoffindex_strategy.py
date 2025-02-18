import backtrader as bt
from ..base_strategy import FlexibleStrategy

class StochasticMomentumIndex_HerrickPayoffIndex_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von StochasticMomentumIndex und HerrickPayoffIndex
    """
    
    params = (
        ('indicators', {
            'StochasticMomentumIndex': {
                'class': StochasticMomentumIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_StochasticMomentumIndex'>
            },
            'HerrickPayoffIndex': {
                'class': HerrickPayoffIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HerrickPayoffIndex'>
            }
        }),
        ('weights', {
            'StochasticMomentumIndex': 1.0,
            'HerrickPayoffIndex': 1.0
        })
    )
