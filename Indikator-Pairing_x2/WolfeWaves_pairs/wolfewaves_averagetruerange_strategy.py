import backtrader as bt
from ..base_strategy import FlexibleStrategy

class WolfeWaves_AverageTrueRange_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von WolfeWaves und AverageTrueRange
    """
    
    params = (
        ('indicators', {
            'WolfeWaves': {
                'class': WolfeWaves,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_WolfeWaves'>
            },
            'AverageTrueRange': {
                'class': AverageTrueRange,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AverageTrueRange1'>
            }
        }),
        ('weights', {
            'WolfeWaves': 1.0,
            'AverageTrueRange': 1.0
        })
    )
