import backtrader as bt
from ..base_strategy import FlexibleStrategy

class DeltaProfile_PriceSquawk_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von DeltaProfile und PriceSquawk
    """
    
    params = (
        ('indicators', {
            'DeltaProfile': {
                'class': DeltaProfile,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_DeltaProfile'>
            },
            'PriceSquawk': {
                'class': PriceSquawk,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PriceSquawk'>
            }
        }),
        ('weights', {
            'DeltaProfile': 1.0,
            'PriceSquawk': 1.0
        })
    )
