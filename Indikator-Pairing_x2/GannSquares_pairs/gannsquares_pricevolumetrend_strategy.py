import backtrader as bt
from ..base_strategy import FlexibleStrategy

class GannSquares_PriceVolumeTrend_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von GannSquares und PriceVolumeTrend
    """
    
    params = (
        ('indicators', {
            'GannSquares': {
                'class': GannSquares,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_GannSquares'>
            },
            'PriceVolumeTrend': {
                'class': PriceVolumeTrend,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PriceVolumeTrend'>
            }
        }),
        ('weights', {
            'GannSquares': 1.0,
            'PriceVolumeTrend': 1.0
        })
    )
