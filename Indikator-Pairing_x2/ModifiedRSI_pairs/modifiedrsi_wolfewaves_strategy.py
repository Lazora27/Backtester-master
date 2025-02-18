import backtrader as bt
from ..base_strategy import FlexibleStrategy

class ModifiedRSI_WolfeWaves_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von ModifiedRSI und WolfeWaves
    """
    
    params = (
        ('indicators', {
            'ModifiedRSI': {
                'class': ModifiedRSI,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ModifiedRSI'>
            },
            'WolfeWaves': {
                'class': WolfeWaves,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_WolfeWaves'>
            }
        }),
        ('weights', {
            'ModifiedRSI': 1.0,
            'WolfeWaves': 1.0
        })
    )
