import backtrader as bt
from ..base_strategy import FlexibleStrategy

class KDJIndicator_WolfeWaves_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von KDJIndicator und WolfeWaves
    """
    
    params = (
        ('indicators', {
            'KDJIndicator': {
                'class': KDJIndicator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_KDJIndicator'>
            },
            'WolfeWaves': {
                'class': WolfeWaves,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_WolfeWaves'>
            }
        }),
        ('weights', {
            'KDJIndicator': 1.0,
            'WolfeWaves': 1.0
        })
    )
