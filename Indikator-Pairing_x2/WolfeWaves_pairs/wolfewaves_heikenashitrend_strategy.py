import backtrader as bt
from ..base_strategy import FlexibleStrategy

class WolfeWaves_HeikenAshiTrend_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von WolfeWaves und HeikenAshiTrend
    """
    
    params = (
        ('indicators', {
            'WolfeWaves': {
                'class': WolfeWaves,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_WolfeWaves'>
            },
            'HeikenAshiTrend': {
                'class': HeikenAshiTrend,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HeikenAshiTrend'>
            }
        }),
        ('weights', {
            'WolfeWaves': 1.0,
            'HeikenAshiTrend': 1.0
        })
    )
