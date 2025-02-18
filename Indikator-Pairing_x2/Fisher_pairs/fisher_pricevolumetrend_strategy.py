import backtrader as bt
from ..base_strategy import FlexibleStrategy

class Fisher_PriceVolumeTrend_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von Fisher und PriceVolumeTrend
    """
    
    params = (
        ('indicators', {
            'Fisher': {
                'class': Fisher,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_Fisher'>
            },
            'PriceVolumeTrend': {
                'class': PriceVolumeTrend,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PriceVolumeTrend'>
            }
        }),
        ('weights', {
            'Fisher': 1.0,
            'PriceVolumeTrend': 1.0
        })
    )
