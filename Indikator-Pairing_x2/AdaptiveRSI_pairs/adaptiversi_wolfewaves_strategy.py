import backtrader as bt
from ..base_strategy import FlexibleStrategy

class AdaptiveRSI_WolfeWaves_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von AdaptiveRSI und WolfeWaves
    """
    
    params = (
        ('indicators', {
            'AdaptiveRSI': {
                'class': AdaptiveRSI,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AdaptiveRSI'>
            },
            'WolfeWaves': {
                'class': WolfeWaves,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_WolfeWaves'>
            }
        }),
        ('weights', {
            'AdaptiveRSI': 1.0,
            'WolfeWaves': 1.0
        })
    )
