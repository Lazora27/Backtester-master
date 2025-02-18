import backtrader as bt
from ..base_strategy import FlexibleStrategy

class StochasticDivergence_AutoSupportResistance_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von StochasticDivergence und AutoSupportResistance
    """
    
    params = (
        ('indicators', {
            'StochasticDivergence': {
                'class': StochasticDivergence,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_StochasticDivergence'>
            },
            'AutoSupportResistance': {
                'class': AutoSupportResistance,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AutoSupportResistance'>
            }
        }),
        ('weights', {
            'StochasticDivergence': 1.0,
            'AutoSupportResistance': 1.0
        })
    )
