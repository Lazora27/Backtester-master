import backtrader as bt
from ..base_strategy import FlexibleStrategy

class WolfeWaves_BollingerPercentB_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von WolfeWaves und BollingerPercentB
    """
    
    params = (
        ('indicators', {
            'WolfeWaves': {
                'class': WolfeWaves,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_WolfeWaves'>
            },
            'BollingerPercentB': {
                'class': BollingerPercentB,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_BollingerPercentB'>
            }
        }),
        ('weights', {
            'WolfeWaves': 1.0,
            'BollingerPercentB': 1.0
        })
    )
