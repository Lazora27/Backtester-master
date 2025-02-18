import backtrader as bt
from ..base_strategy import FlexibleStrategy

class SmoothedRSI_WolfeWaves_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von SmoothedRSI und WolfeWaves
    """
    
    params = (
        ('indicators', {
            'SmoothedRSI': {
                'class': SmoothedRSI,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SmoothedRSI'>
            },
            'WolfeWaves': {
                'class': WolfeWaves,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_WolfeWaves'>
            }
        }),
        ('weights', {
            'SmoothedRSI': 1.0,
            'WolfeWaves': 1.0
        })
    )
