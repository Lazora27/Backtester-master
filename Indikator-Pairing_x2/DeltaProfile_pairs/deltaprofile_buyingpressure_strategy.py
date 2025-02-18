import backtrader as bt
from ..base_strategy import FlexibleStrategy

class DeltaProfile_BuyingPressure_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von DeltaProfile und BuyingPressure
    """
    
    params = (
        ('indicators', {
            'DeltaProfile': {
                'class': DeltaProfile,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_DeltaProfile'>
            },
            'BuyingPressure': {
                'class': BuyingPressure,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_BuyingPressure'>
            }
        }),
        ('weights', {
            'DeltaProfile': 1.0,
            'BuyingPressure': 1.0
        })
    )
