import backtrader as bt
from ..base_strategy import FlexibleStrategy

class DeltaProfile_MarketCycleIndicator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von DeltaProfile und MarketCycleIndicator
    """
    
    params = (
        ('indicators', {
            'DeltaProfile': {
                'class': DeltaProfile,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_DeltaProfile'>
            },
            'MarketCycleIndicator': {
                'class': MarketCycleIndicator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MarketCycleIndicator'>
            }
        }),
        ('weights', {
            'DeltaProfile': 1.0,
            'MarketCycleIndicator': 1.0
        })
    )
