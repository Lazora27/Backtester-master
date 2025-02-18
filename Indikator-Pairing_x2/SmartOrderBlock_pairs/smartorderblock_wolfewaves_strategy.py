import backtrader as bt
from ..base_strategy import FlexibleStrategy

class SmartOrderBlock_WolfeWaves_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von SmartOrderBlock und WolfeWaves
    """
    
    params = (
        ('indicators', {
            'SmartOrderBlock': {
                'class': SmartOrderBlock,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SmartOrderBlock'>
            },
            'WolfeWaves': {
                'class': WolfeWaves,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_WolfeWaves'>
            }
        }),
        ('weights', {
            'SmartOrderBlock': 1.0,
            'WolfeWaves': 1.0
        })
    )
