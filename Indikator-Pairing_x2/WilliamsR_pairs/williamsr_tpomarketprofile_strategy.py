import backtrader as bt
from ..base_strategy import FlexibleStrategy

class WilliamsR_TPOMarketProfile_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von WilliamsR und TPOMarketProfile
    """
    
    params = (
        ('indicators', {
            'WilliamsR': {
                'class': WilliamsR,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_WilliamsR1'>
            },
            'TPOMarketProfile': {
                'class': TPOMarketProfile,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TPOMarketProfile'>
            }
        }),
        ('weights', {
            'WilliamsR': 1.0,
            'TPOMarketProfile': 1.0
        })
    )
