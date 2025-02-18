import backtrader as bt
from ..base_strategy import FlexibleStrategy

class PriceRateOfChange_TPOMarketProfile_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von PriceRateOfChange und TPOMarketProfile
    """
    
    params = (
        ('indicators', {
            'PriceRateOfChange': {
                'class': PriceRateOfChange,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PriceRateOfChange'>
            },
            'TPOMarketProfile': {
                'class': TPOMarketProfile,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TPOMarketProfile'>
            }
        }),
        ('weights', {
            'PriceRateOfChange': 1.0,
            'TPOMarketProfile': 1.0
        })
    )
