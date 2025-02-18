import backtrader as bt
from ..base_strategy import FlexibleStrategy

class WolfeWaves_PriceVolumeTrend_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von WolfeWaves und PriceVolumeTrend
    """
    
    params = (
        ('indicators', {
            'WolfeWaves': {
                'class': WolfeWaves,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_WolfeWaves'>
            },
            'PriceVolumeTrend': {
                'class': PriceVolumeTrend,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PriceVolumeTrend'>
            }
        }),
        ('weights', {
            'WolfeWaves': 1.0,
            'PriceVolumeTrend': 1.0
        })
    )
