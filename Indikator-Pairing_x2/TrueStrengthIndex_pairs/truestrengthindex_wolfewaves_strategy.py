import backtrader as bt
from ..base_strategy import FlexibleStrategy

class TrueStrengthIndex_WolfeWaves_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von TrueStrengthIndex und WolfeWaves
    """
    
    params = (
        ('indicators', {
            'TrueStrengthIndex': {
                'class': TrueStrengthIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TrueStrengthIndex'>
            },
            'WolfeWaves': {
                'class': WolfeWaves,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_WolfeWaves'>
            }
        }),
        ('weights', {
            'TrueStrengthIndex': 1.0,
            'WolfeWaves': 1.0
        })
    )
