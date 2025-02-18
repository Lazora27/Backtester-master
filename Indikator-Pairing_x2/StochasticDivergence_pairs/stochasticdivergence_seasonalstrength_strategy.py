import backtrader as bt
from ..base_strategy import FlexibleStrategy

class StochasticDivergence_SeasonalStrength_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von StochasticDivergence und SeasonalStrength
    """
    
    params = (
        ('indicators', {
            'StochasticDivergence': {
                'class': StochasticDivergence,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_StochasticDivergence'>
            },
            'SeasonalStrength': {
                'class': SeasonalStrength,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SeasonalStrength'>
            }
        }),
        ('weights', {
            'StochasticDivergence': 1.0,
            'SeasonalStrength': 1.0
        })
    )
