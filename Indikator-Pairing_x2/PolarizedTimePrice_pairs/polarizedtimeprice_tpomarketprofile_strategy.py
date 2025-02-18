import backtrader as bt
from ..base_strategy import FlexibleStrategy

class PolarizedTimePrice_TPOMarketProfile_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von PolarizedTimePrice und TPOMarketProfile
    """
    
    params = (
        ('indicators', {
            'PolarizedTimePrice': {
                'class': PolarizedTimePrice,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PolarizedTimePrice'>
            },
            'TPOMarketProfile': {
                'class': TPOMarketProfile,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TPOMarketProfile'>
            }
        }),
        ('weights', {
            'PolarizedTimePrice': 1.0,
            'TPOMarketProfile': 1.0
        })
    )
