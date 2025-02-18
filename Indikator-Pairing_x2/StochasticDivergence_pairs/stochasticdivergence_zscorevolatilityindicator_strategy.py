import backtrader as bt
from ..base_strategy import FlexibleStrategy

class StochasticDivergence_ZScoreVolatilityIndicator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von StochasticDivergence und ZScoreVolatilityIndicator
    """
    
    params = (
        ('indicators', {
            'StochasticDivergence': {
                'class': StochasticDivergence,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_StochasticDivergence'>
            },
            'ZScoreVolatilityIndicator': {
                'class': ZScoreVolatilityIndicator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ZScoreVolatilityIndicator'>
            }
        }),
        ('weights', {
            'StochasticDivergence': 1.0,
            'ZScoreVolatilityIndicator': 1.0
        })
    )
