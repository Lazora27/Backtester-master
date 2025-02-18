import backtrader as bt
from ..base_strategy import FlexibleStrategy

class ChaikinOscillator_WolfeWaves_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von ChaikinOscillator und WolfeWaves
    """
    
    params = (
        ('indicators', {
            'ChaikinOscillator': {
                'class': ChaikinOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ChaikinOscillator'>
            },
            'WolfeWaves': {
                'class': WolfeWaves,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_WolfeWaves'>
            }
        }),
        ('weights', {
            'ChaikinOscillator': 1.0,
            'WolfeWaves': 1.0
        })
    )
