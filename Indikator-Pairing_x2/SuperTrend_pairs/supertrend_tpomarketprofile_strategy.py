import backtrader as bt
from ..base_strategy import FlexibleStrategy

class SuperTrend_TPOMarketProfile_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von SuperTrend und TPOMarketProfile
    """
    
    params = (
        ('indicators', {
            'SuperTrend': {
                'class': SuperTrend,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SuperTrend'>
            },
            'TPOMarketProfile': {
                'class': TPOMarketProfile,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TPOMarketProfile'>
            }
        }),
        ('weights', {
            'SuperTrend': 1.0,
            'TPOMarketProfile': 1.0
        })
    )
