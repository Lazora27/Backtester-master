import backtrader as bt
from ..base_strategy import FlexibleStrategy

class TwoPeriodRSI_TPOMarketProfile_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von TwoPeriodRSI und TPOMarketProfile
    """
    
    params = (
        ('indicators', {
            'TwoPeriodRSI': {
                'class': TwoPeriodRSI,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TwoPeriodRSI'>
            },
            'TPOMarketProfile': {
                'class': TPOMarketProfile,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TPOMarketProfile'>
            }
        }),
        ('weights', {
            'TwoPeriodRSI': 1.0,
            'TPOMarketProfile': 1.0
        })
    )
