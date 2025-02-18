import backtrader as bt
from ..base_strategy import FlexibleStrategy

class CumulativeTick_TPOMarketProfile_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von CumulativeTick und TPOMarketProfile
    """
    
    params = (
        ('indicators', {
            'CumulativeTick': {
                'class': CumulativeTick,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CumulativeTick'>
            },
            'TPOMarketProfile': {
                'class': TPOMarketProfile,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TPOMarketProfile'>
            }
        }),
        ('weights', {
            'CumulativeTick': 1.0,
            'TPOMarketProfile': 1.0
        })
    )
