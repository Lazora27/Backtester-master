import backtrader as bt
from ..base_strategy import FlexibleStrategy

class WolfeWaves_BarStrength_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von WolfeWaves und BarStrength
    """
    
    params = (
        ('indicators', {
            'WolfeWaves': {
                'class': WolfeWaves,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_WolfeWaves'>
            },
            'BarStrength': {
                'class': BarStrength,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_BarStrength'>
            }
        }),
        ('weights', {
            'WolfeWaves': 1.0,
            'BarStrength': 1.0
        })
    )
