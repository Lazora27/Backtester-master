import backtrader as bt
from ..base_strategy import FlexibleStrategy

class TrendExhaustion_TPOMarketProfile_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von TrendExhaustion und TPOMarketProfile
    """
    
    params = (
        ('indicators', {
            'TrendExhaustion': {
                'class': TrendExhaustion,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TrendExhaustion'>
            },
            'TPOMarketProfile': {
                'class': TPOMarketProfile,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TPOMarketProfile'>
            }
        }),
        ('weights', {
            'TrendExhaustion': 1.0,
            'TPOMarketProfile': 1.0
        })
    )
