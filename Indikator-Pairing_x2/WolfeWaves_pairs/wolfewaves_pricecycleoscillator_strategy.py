import backtrader as bt
from ..base_strategy import FlexibleStrategy

class WolfeWaves_PriceCycleOscillator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von WolfeWaves und PriceCycleOscillator
    """
    
    params = (
        ('indicators', {
            'WolfeWaves': {
                'class': WolfeWaves,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_WolfeWaves'>
            },
            'PriceCycleOscillator': {
                'class': PriceCycleOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PriceCycleOscillator'>
            }
        }),
        ('weights', {
            'WolfeWaves': 1.0,
            'PriceCycleOscillator': 1.0
        })
    )
