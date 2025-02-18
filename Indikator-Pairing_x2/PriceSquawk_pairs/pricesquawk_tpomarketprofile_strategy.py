import backtrader as bt
from ..base_strategy import FlexibleStrategy

class PriceSquawk_TPOMarketProfile_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von PriceSquawk und TPOMarketProfile
    """
    
    params = (
        ('indicators', {
            'PriceSquawk': {
                'class': PriceSquawk,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PriceSquawk'>
            },
            'TPOMarketProfile': {
                'class': TPOMarketProfile,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TPOMarketProfile'>
            }
        }),
        ('weights', {
            'PriceSquawk': 1.0,
            'TPOMarketProfile': 1.0
        })
    )
