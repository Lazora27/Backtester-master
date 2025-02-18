import backtrader as bt
from ..base_strategy import FlexibleStrategy

class GannFans_PriceVolumeTrend_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von GannFans und PriceVolumeTrend
    """
    
    params = (
        ('indicators', {
            'GannFans': {
                'class': GannFans,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_GannFans'>
            },
            'PriceVolumeTrend': {
                'class': PriceVolumeTrend,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PriceVolumeTrend'>
            }
        }),
        ('weights', {
            'GannFans': 1.0,
            'PriceVolumeTrend': 1.0
        })
    )
