import backtrader as bt
from ..base_strategy import FlexibleStrategy

class MomentumTrendStrength_TPOMarketProfile_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von MomentumTrendStrength und TPOMarketProfile
    """
    
    params = (
        ('indicators', {
            'MomentumTrendStrength': {
                'class': MomentumTrendStrength,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MomentumTrendStrength'>
            },
            'TPOMarketProfile': {
                'class': TPOMarketProfile,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TPOMarketProfile'>
            }
        }),
        ('weights', {
            'MomentumTrendStrength': 1.0,
            'TPOMarketProfile': 1.0
        })
    )
