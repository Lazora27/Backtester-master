import backtrader as bt
from ..base_strategy import FlexibleStrategy

class WolfeWaves_KeltnerBandWidth_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von WolfeWaves und KeltnerBandWidth
    """
    
    params = (
        ('indicators', {
            'WolfeWaves': {
                'class': WolfeWaves,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_WolfeWaves'>
            },
            'KeltnerBandWidth': {
                'class': KeltnerBandWidth,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_KeltnerBandWidth'>
            }
        }),
        ('weights', {
            'WolfeWaves': 1.0,
            'KeltnerBandWidth': 1.0
        })
    )
