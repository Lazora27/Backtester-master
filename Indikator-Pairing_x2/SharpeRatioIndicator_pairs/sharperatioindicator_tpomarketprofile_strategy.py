import backtrader as bt
from ..base_strategy import FlexibleStrategy

class SharpeRatioIndicator_TPOMarketProfile_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von SharpeRatioIndicator und TPOMarketProfile
    """
    
    params = (
        ('indicators', {
            'SharpeRatioIndicator': {
                'class': SharpeRatioIndicator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SharpeRatioIndicator'>
            },
            'TPOMarketProfile': {
                'class': TPOMarketProfile,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TPOMarketProfile'>
            }
        }),
        ('weights', {
            'SharpeRatioIndicator': 1.0,
            'TPOMarketProfile': 1.0
        })
    )
