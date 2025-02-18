import backtrader as bt
from ..base_strategy import FlexibleStrategy

class StochasticDivergence_MarketFacilitationIndex_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von StochasticDivergence und MarketFacilitationIndex
    """
    
    params = (
        ('indicators', {
            'StochasticDivergence': {
                'class': StochasticDivergence,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_StochasticDivergence'>
            },
            'MarketFacilitationIndex': {
                'class': MarketFacilitationIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MarketFacilitationIndex'>
            }
        }),
        ('weights', {
            'StochasticDivergence': 1.0,
            'MarketFacilitationIndex': 1.0
        })
    )
