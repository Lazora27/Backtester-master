import backtrader as bt
from ..base_strategy import FlexibleStrategy

class TrendExhaustion_ChandeKrollStop_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von TrendExhaustion und ChandeKrollStop
    """
    
    params = (
        ('indicators', {
            'TrendExhaustion': {
                'class': TrendExhaustion,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TrendExhaustion'>
            },
            'ChandeKrollStop': {
                'class': ChandeKrollStop,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ChandeKrollStop'>
            }
        }),
        ('weights', {
            'TrendExhaustion': 1.0,
            'ChandeKrollStop': 1.0
        })
    )
