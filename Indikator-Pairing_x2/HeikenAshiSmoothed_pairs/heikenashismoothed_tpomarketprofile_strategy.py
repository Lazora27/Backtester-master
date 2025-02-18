import backtrader as bt
from ..base_strategy import FlexibleStrategy

class HeikenAshiSmoothed_TPOMarketProfile_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von HeikenAshiSmoothed und TPOMarketProfile
    """
    
    params = (
        ('indicators', {
            'HeikenAshiSmoothed': {
                'class': HeikenAshiSmoothed,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HeikenAshiSmoothed'>
            },
            'TPOMarketProfile': {
                'class': TPOMarketProfile,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TPOMarketProfile'>
            }
        }),
        ('weights', {
            'HeikenAshiSmoothed': 1.0,
            'TPOMarketProfile': 1.0
        })
    )
