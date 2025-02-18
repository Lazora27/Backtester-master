import backtrader as bt
from ..base_strategy import FlexibleStrategy

class ChaikinVolatility_TPOMarketProfile_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von ChaikinVolatility und TPOMarketProfile
    """
    
    params = (
        ('indicators', {
            'ChaikinVolatility': {
                'class': ChaikinVolatility,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ChaikinVolatility'>
            },
            'TPOMarketProfile': {
                'class': TPOMarketProfile,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TPOMarketProfile'>
            }
        }),
        ('weights', {
            'ChaikinVolatility': 1.0,
            'TPOMarketProfile': 1.0
        })
    )
