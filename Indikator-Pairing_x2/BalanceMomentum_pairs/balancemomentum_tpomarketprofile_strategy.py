import backtrader as bt
from ..base_strategy import FlexibleStrategy

class BalanceMomentum_TPOMarketProfile_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von BalanceMomentum und TPOMarketProfile
    """
    
    params = (
        ('indicators', {
            'BalanceMomentum': {
                'class': BalanceMomentum,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_BalanceMomentum'>
            },
            'TPOMarketProfile': {
                'class': TPOMarketProfile,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TPOMarketProfile'>
            }
        }),
        ('weights', {
            'BalanceMomentum': 1.0,
            'TPOMarketProfile': 1.0
        })
    )
