import backtrader as bt
from ..base_strategy import FlexibleStrategy

class WolfeWaves_BollingerBandWidth_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von WolfeWaves und BollingerBandWidth
    """
    
    params = (
        ('indicators', {
            'WolfeWaves': {
                'class': WolfeWaves,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_WolfeWaves'>
            },
            'BollingerBandWidth': {
                'class': BollingerBandWidth,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_BollingerBandWidth'>
            }
        }),
        ('weights', {
            'WolfeWaves': 1.0,
            'BollingerBandWidth': 1.0
        })
    )
