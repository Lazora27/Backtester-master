import backtrader as bt
from ..base_strategy import FlexibleStrategy

class WolfeWaves_CyberCycle_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von WolfeWaves und CyberCycle
    """
    
    params = (
        ('indicators', {
            'WolfeWaves': {
                'class': WolfeWaves,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_WolfeWaves'>
            },
            'CyberCycle': {
                'class': CyberCycle,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CyberCycle'>
            }
        }),
        ('weights', {
            'WolfeWaves': 1.0,
            'CyberCycle': 1.0
        })
    )
