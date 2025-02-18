import backtrader as bt
from ..base_strategy import FlexibleStrategy

class GannSquareReversal_PriceVolumeTrend_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von GannSquareReversal und PriceVolumeTrend
    """
    
    params = (
        ('indicators', {
            'GannSquareReversal': {
                'class': GannSquareReversal,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_GannSquareReversal'>
            },
            'PriceVolumeTrend': {
                'class': PriceVolumeTrend,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PriceVolumeTrend'>
            }
        }),
        ('weights', {
            'GannSquareReversal': 1.0,
            'PriceVolumeTrend': 1.0
        })
    )
