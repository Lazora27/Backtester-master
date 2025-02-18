import backtrader as bt
from ..base_strategy import FlexibleStrategy

class OpenInterest_PriceVolumeTrend_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von OpenInterest und PriceVolumeTrend
    """
    
    params = (
        ('indicators', {
            'OpenInterest': {
                'class': OpenInterest,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_OpenInterest'>
            },
            'PriceVolumeTrend': {
                'class': PriceVolumeTrend,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PriceVolumeTrend'>
            }
        }),
        ('weights', {
            'OpenInterest': 1.0,
            'PriceVolumeTrend': 1.0
        })
    )
