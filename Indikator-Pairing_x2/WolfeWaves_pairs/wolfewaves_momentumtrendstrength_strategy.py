import backtrader as bt
from ..base_strategy import FlexibleStrategy

class WolfeWaves_MomentumTrendStrength_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von WolfeWaves und MomentumTrendStrength
    """
    
    params = (
        ('indicators', {
            'WolfeWaves': {
                'class': WolfeWaves,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_WolfeWaves'>
            },
            'MomentumTrendStrength': {
                'class': MomentumTrendStrength,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MomentumTrendStrength'>
            }
        }),
        ('weights', {
            'WolfeWaves': 1.0,
            'MomentumTrendStrength': 1.0
        })
    )
