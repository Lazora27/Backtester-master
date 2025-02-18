import backtrader as bt
from ..base_strategy import FlexibleStrategy

class StochasticTrendStrength_CyberCycleOscillator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von StochasticTrendStrength und CyberCycleOscillator
    """
    
    params = (
        ('indicators', {
            'StochasticTrendStrength': {
                'class': StochasticTrendStrength,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_StochasticTrendStrength'>
            },
            'CyberCycleOscillator': {
                'class': CyberCycleOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CyberCycleOscillator'>
            }
        }),
        ('weights', {
            'StochasticTrendStrength': 1.0,
            'CyberCycleOscillator': 1.0
        })
    )
