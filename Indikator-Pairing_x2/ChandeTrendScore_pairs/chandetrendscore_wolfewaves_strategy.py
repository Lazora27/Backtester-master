import backtrader as bt
from ..base_strategy import FlexibleStrategy

class ChandeTrendScore_WolfeWaves_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von ChandeTrendScore und WolfeWaves
    """
    
    params = (
        ('indicators', {
            'ChandeTrendScore': {
                'class': ChandeTrendScore,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ChandeTrendScore'>
            },
            'WolfeWaves': {
                'class': WolfeWaves,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_WolfeWaves'>
            }
        }),
        ('weights', {
            'ChandeTrendScore': 1.0,
            'WolfeWaves': 1.0
        })
    )
