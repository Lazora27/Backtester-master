import backtrader as bt
from ..base_strategy import FlexibleStrategy

class PriceDelta_IchimokuCloud_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von PriceDelta und IchimokuCloud
    """
    
    params = (
        ('indicators', {
            'PriceDelta': {
                'class': PriceDelta,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PriceDelta'>
            },
            'IchimokuCloud': {
                'class': IchimokuCloud,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_IchimokuCloud'>
            }
        }),
        ('weights', {
            'PriceDelta': 1.0,
            'IchimokuCloud': 1.0
        })
    )
