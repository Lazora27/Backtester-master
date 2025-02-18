import backtrader as bt
from ..base_strategy import FlexibleStrategy

class DeltaProfile_TRIXIndicator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von DeltaProfile und TRIXIndicator
    """
    
    params = (
        ('indicators', {
            'DeltaProfile': {
                'class': DeltaProfile,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_DeltaProfile'>
            },
            'TRIXIndicator': {
                'class': TRIXIndicator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TRIXIndicator'>
            }
        }),
        ('weights', {
            'DeltaProfile': 1.0,
            'TRIXIndicator': 1.0
        })
    )
