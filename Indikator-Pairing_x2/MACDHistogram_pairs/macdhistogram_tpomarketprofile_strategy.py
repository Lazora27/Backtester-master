import backtrader as bt
from ..base_strategy import FlexibleStrategy

class MACDHistogram_TPOMarketProfile_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von MACDHistogram und TPOMarketProfile
    """
    
    params = (
        ('indicators', {
            'MACDHistogram': {
                'class': MACDHistogram,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MACDHistogram'>
            },
            'TPOMarketProfile': {
                'class': TPOMarketProfile,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TPOMarketProfile'>
            }
        }),
        ('weights', {
            'MACDHistogram': 1.0,
            'TPOMarketProfile': 1.0
        })
    )
