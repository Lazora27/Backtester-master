import backtrader as bt
from ..base_strategy import FlexibleStrategy

class StochasticDivergence_AverageTrueRange_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von StochasticDivergence und AverageTrueRange
    """
    
    params = (
        ('indicators', {
            'StochasticDivergence': {
                'class': StochasticDivergence,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_StochasticDivergence'>
            },
            'AverageTrueRange': {
                'class': AverageTrueRange,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AverageTrueRange1'>
            }
        }),
        ('weights', {
            'StochasticDivergence': 1.0,
            'AverageTrueRange': 1.0
        })
    )
