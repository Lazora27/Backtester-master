import backtrader as bt
from ..base_strategy import FlexibleStrategy

class DeltaProfile_PolarizedTimePrice_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von DeltaProfile und PolarizedTimePrice
    """
    
    params = (
        ('indicators', {
            'DeltaProfile': {
                'class': DeltaProfile,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_DeltaProfile'>
            },
            'PolarizedTimePrice': {
                'class': PolarizedTimePrice,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PolarizedTimePrice'>
            }
        }),
        ('weights', {
            'DeltaProfile': 1.0,
            'PolarizedTimePrice': 1.0
        })
    )
