import backtrader as bt
from ..base_strategy import FlexibleStrategy

class DeltaProfile_MarketOrderFlow_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von DeltaProfile und MarketOrderFlow
    """
    
    params = (
        ('indicators', {
            'DeltaProfile': {
                'class': DeltaProfile,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_DeltaProfile'>
            },
            'MarketOrderFlow': {
                'class': MarketOrderFlow,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MarketOrderFlow'>
            }
        }),
        ('weights', {
            'DeltaProfile': 1.0,
            'MarketOrderFlow': 1.0
        })
    )
