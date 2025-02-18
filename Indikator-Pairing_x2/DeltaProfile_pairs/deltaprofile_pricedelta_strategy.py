import backtrader as bt
from ..base_strategy import FlexibleStrategy

class DeltaProfile_PriceDelta_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von DeltaProfile und PriceDelta
    """
    
    params = (
        ('indicators', {
            'DeltaProfile': {
                'class': DeltaProfile,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_DeltaProfile'>
            },
            'PriceDelta': {
                'class': PriceDelta,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PriceDelta'>
            }
        }),
        ('weights', {
            'DeltaProfile': 1.0,
            'PriceDelta': 1.0
        })
    )
