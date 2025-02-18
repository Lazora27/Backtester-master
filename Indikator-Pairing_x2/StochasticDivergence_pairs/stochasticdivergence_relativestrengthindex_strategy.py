import backtrader as bt
from ..base_strategy import FlexibleStrategy

class StochasticDivergence_RelativeStrengthIndex_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von StochasticDivergence und RelativeStrengthIndex
    """
    
    params = (
        ('indicators', {
            'StochasticDivergence': {
                'class': StochasticDivergence,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_StochasticDivergence'>
            },
            'RelativeStrengthIndex': {
                'class': RelativeStrengthIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_RelativeStrengthIndex1'>
            }
        }),
        ('weights', {
            'StochasticDivergence': 1.0,
            'RelativeStrengthIndex': 1.0
        })
    )
