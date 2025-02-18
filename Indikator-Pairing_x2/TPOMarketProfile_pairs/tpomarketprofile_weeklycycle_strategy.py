import backtrader as bt
from ..base_strategy import FlexibleStrategy

class TPOMarketProfile_WeeklyCycle_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von TPOMarketProfile und WeeklyCycle
    """
    
    params = (
        ('indicators', {
            'TPOMarketProfile': {
                'class': TPOMarketProfile,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TPOMarketProfile'>
            },
            'WeeklyCycle': {
                'class': WeeklyCycle,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_WeeklyCycle'>
            }
        }),
        ('weights', {
            'TPOMarketProfile': 1.0,
            'WeeklyCycle': 1.0
        })
    )
