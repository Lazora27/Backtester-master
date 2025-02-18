import backtrader as bt
from ..base_strategy import FlexibleStrategy

class DeltaProfile_RoundNumbersIndicator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von DeltaProfile und RoundNumbersIndicator
    """
    
    params = (
        ('indicators', {
            'DeltaProfile': {
                'class': DeltaProfile,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_DeltaProfile'>
            },
            'RoundNumbersIndicator': {
                'class': RoundNumbersIndicator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_RoundNumbersIndicator'>
            }
        }),
        ('weights', {
            'DeltaProfile': 1.0,
            'RoundNumbersIndicator': 1.0
        })
    )
