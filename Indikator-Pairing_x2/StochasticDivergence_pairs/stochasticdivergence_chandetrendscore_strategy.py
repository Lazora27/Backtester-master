import backtrader as bt
from ..base_strategy import FlexibleStrategy

class StochasticDivergence_ChandeTrendScore_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von StochasticDivergence und ChandeTrendScore
    """
    
    params = (
        ('indicators', {
            'StochasticDivergence': {
                'class': StochasticDivergence,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_StochasticDivergence'>
            },
            'ChandeTrendScore': {
                'class': ChandeTrendScore,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ChandeTrendScore'>
            }
        }),
        ('weights', {
            'StochasticDivergence': 1.0,
            'ChandeTrendScore': 1.0
        })
    )
