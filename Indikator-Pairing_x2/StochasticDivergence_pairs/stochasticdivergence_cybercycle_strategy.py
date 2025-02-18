import backtrader as bt
from ..base_strategy import FlexibleStrategy

class StochasticDivergence_CyberCycle_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von StochasticDivergence und CyberCycle
    """
    
    params = (
        ('indicators', {
            'StochasticDivergence': {
                'class': StochasticDivergence,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_StochasticDivergence'>
            },
            'CyberCycle': {
                'class': CyberCycle,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CyberCycle'>
            }
        }),
        ('weights', {
            'StochasticDivergence': 1.0,
            'CyberCycle': 1.0
        })
    )
