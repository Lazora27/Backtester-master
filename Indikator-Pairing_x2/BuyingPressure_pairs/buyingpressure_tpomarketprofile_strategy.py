import backtrader as bt
from ..base_strategy import FlexibleStrategy

class BuyingPressure_TPOMarketProfile_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von BuyingPressure und TPOMarketProfile
    """
    
    params = (
        ('indicators', {
            'BuyingPressure': {
                'class': BuyingPressure,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_BuyingPressure'>
            },
            'TPOMarketProfile': {
                'class': TPOMarketProfile,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TPOMarketProfile'>
            }
        }),
        ('weights', {
            'BuyingPressure': 1.0,
            'TPOMarketProfile': 1.0
        })
    )
