import backtrader as bt
from ..base_strategy import FlexibleStrategy

class DeltaProfile_OpenInterest_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von DeltaProfile und OpenInterest
    """
    
    params = (
        ('indicators', {
            'DeltaProfile': {
                'class': DeltaProfile,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_DeltaProfile'>
            },
            'OpenInterest': {
                'class': OpenInterest,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_OpenInterest'>
            }
        }),
        ('weights', {
            'DeltaProfile': 1.0,
            'OpenInterest': 1.0
        })
    )
