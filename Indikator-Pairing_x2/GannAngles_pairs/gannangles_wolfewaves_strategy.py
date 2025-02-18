import backtrader as bt
from ..base_strategy import FlexibleStrategy

class GannAngles_WolfeWaves_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von GannAngles und WolfeWaves
    """
    
    params = (
        ('indicators', {
            'GannAngles': {
                'class': GannAngles,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_GannAngles1'>
            },
            'WolfeWaves': {
                'class': WolfeWaves,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_WolfeWaves'>
            }
        }),
        ('weights', {
            'GannAngles': 1.0,
            'WolfeWaves': 1.0
        })
    )
