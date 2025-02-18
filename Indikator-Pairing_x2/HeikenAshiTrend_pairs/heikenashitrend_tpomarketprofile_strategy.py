import backtrader as bt
from ..base_strategy import FlexibleStrategy

class HeikenAshiTrend_TPOMarketProfile_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von HeikenAshiTrend und TPOMarketProfile
    """
    
    params = (
        ('indicators', {
            'HeikenAshiTrend': {
                'class': HeikenAshiTrend,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HeikenAshiTrend'>
            },
            'TPOMarketProfile': {
                'class': TPOMarketProfile,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TPOMarketProfile'>
            }
        }),
        ('weights', {
            'HeikenAshiTrend': 1.0,
            'TPOMarketProfile': 1.0
        })
    )
