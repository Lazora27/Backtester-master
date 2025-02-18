import backtrader as bt
from ..base_strategy import FlexibleStrategy

class UltimateOscillator_WolfeWaves_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von UltimateOscillator und WolfeWaves
    """
    
    params = (
        ('indicators', {
            'UltimateOscillator': {
                'class': UltimateOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_UltimateOscillator1'>
            },
            'WolfeWaves': {
                'class': WolfeWaves,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_WolfeWaves'>
            }
        }),
        ('weights', {
            'UltimateOscillator': 1.0,
            'WolfeWaves': 1.0
        })
    )
