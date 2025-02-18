import backtrader as bt
from ..base_strategy import FlexibleStrategy

class WolfeWaves_BollingerBands_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von WolfeWaves und BollingerBands
    """
    
    params = (
        ('indicators', {
            'WolfeWaves': {
                'class': WolfeWaves,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_WolfeWaves'>
            },
            'BollingerBands': {
                'class': BollingerBands,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_BollingerBands1'>
            }
        }),
        ('weights', {
            'WolfeWaves': 1.0,
            'BollingerBands': 1.0
        })
    )
