import backtrader as bt
from ..base_strategy import FlexibleStrategy

class CompositeIndexDivergence_HyperbolicVolatility_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von CompositeIndexDivergence und HyperbolicVolatility
    """
    
    params = (
        ('indicators', {
            'CompositeIndexDivergence': {
                'class': CompositeIndexDivergence,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CompositeIndexDivergence'>
            },
            'HyperbolicVolatility': {
                'class': HyperbolicVolatility,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HyperbolicVolatility'>
            }
        }),
        ('weights', {
            'CompositeIndexDivergence': 1.0,
            'HyperbolicVolatility': 1.0
        })
    )
