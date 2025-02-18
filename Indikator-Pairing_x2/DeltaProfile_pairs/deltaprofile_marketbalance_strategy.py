import backtrader as bt
from ..base_strategy import FlexibleStrategy

class DeltaProfile_MarketBalance_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von DeltaProfile und MarketBalance
    """
    
    params = (
        ('indicators', {
            'DeltaProfile': {
                'class': DeltaProfile,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_DeltaProfile'>
            },
            'MarketBalance': {
                'class': MarketBalance,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MarketBalance'>
            }
        }),
        ('weights', {
            'DeltaProfile': 1.0,
            'MarketBalance': 1.0
        })
    )
