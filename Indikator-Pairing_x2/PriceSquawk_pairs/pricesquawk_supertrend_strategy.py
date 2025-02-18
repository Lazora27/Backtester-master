import backtrader as bt
from ..base_strategy import FlexibleStrategy

class PriceSquawk_SuperTrend_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von PriceSquawk und SuperTrend
    """
    
    params = (
        ('indicators', {
            'PriceSquawk': {
                'class': PriceSquawk,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PriceSquawk'>
            },
            'SuperTrend': {
                'class': SuperTrend,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SuperTrend'>
            }
        }),
        ('weights', {
            'PriceSquawk': 1.0,
            'SuperTrend': 1.0
        })
    )
