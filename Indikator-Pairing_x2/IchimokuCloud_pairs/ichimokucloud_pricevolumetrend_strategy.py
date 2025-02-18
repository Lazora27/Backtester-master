import backtrader as bt
from ..base_strategy import FlexibleStrategy

class IchimokuCloud_PriceVolumeTrend_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von IchimokuCloud und PriceVolumeTrend
    """
    
    params = (
        ('indicators', {
            'IchimokuCloud': {
                'class': IchimokuCloud,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_IchimokuCloud'>
            },
            'PriceVolumeTrend': {
                'class': PriceVolumeTrend,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PriceVolumeTrend'>
            }
        }),
        ('weights', {
            'IchimokuCloud': 1.0,
            'PriceVolumeTrend': 1.0
        })
    )
