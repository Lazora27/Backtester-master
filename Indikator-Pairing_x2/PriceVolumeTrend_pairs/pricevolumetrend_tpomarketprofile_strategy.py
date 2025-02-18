import backtrader as bt
from ..base_strategy import FlexibleStrategy

class PriceVolumeTrend_TPOMarketProfile_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von PriceVolumeTrend und TPOMarketProfile
    """
    
    params = (
        ('indicators', {
            'PriceVolumeTrend': {
                'class': PriceVolumeTrend,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PriceVolumeTrend'>
            },
            'TPOMarketProfile': {
                'class': TPOMarketProfile,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TPOMarketProfile'>
            }
        }),
        ('weights', {
            'PriceVolumeTrend': 1.0,
            'TPOMarketProfile': 1.0
        })
    )
