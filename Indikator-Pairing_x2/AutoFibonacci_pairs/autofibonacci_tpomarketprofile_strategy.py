import backtrader as bt
from ..base_strategy import FlexibleStrategy

class AutoFibonacci_TPOMarketProfile_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von AutoFibonacci und TPOMarketProfile
    """
    
    params = (
        ('indicators', {
            'AutoFibonacci': {
                'class': AutoFibonacci,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AutoFibonacci'>
            },
            'TPOMarketProfile': {
                'class': TPOMarketProfile,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TPOMarketProfile'>
            }
        }),
        ('weights', {
            'AutoFibonacci': 1.0,
            'TPOMarketProfile': 1.0
        })
    )
