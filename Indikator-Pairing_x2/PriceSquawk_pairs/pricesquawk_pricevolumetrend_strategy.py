import backtrader as bt
from ..base_strategy import FlexibleStrategy

class PriceSquawk_PriceVolumeTrend_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von PriceSquawk und PriceVolumeTrend
    """
    
    params = (
        ('indicators', {
            'PriceSquawk': {
                'class': PriceSquawk,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PriceSquawk'>
            },
            'PriceVolumeTrend': {
                'class': PriceVolumeTrend,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PriceVolumeTrend'>
            }
        }),
        ('weights', {
            'PriceSquawk': 1.0,
            'PriceVolumeTrend': 1.0
        })
    )
