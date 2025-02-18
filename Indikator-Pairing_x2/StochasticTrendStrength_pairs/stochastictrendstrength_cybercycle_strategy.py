import backtrader as bt
from ..base_strategy import FlexibleStrategy

class StochasticTrendStrength_CyberCycle_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von StochasticTrendStrength und CyberCycle
    """
    
    params = (
        ('indicators', {
            'StochasticTrendStrength': {
                'class': StochasticTrendStrength,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_StochasticTrendStrength'>
            },
            'CyberCycle': {
                'class': CyberCycle,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CyberCycle'>
            }
        }),
        ('weights', {
            'StochasticTrendStrength': 1.0,
            'CyberCycle': 1.0
        })
    )
