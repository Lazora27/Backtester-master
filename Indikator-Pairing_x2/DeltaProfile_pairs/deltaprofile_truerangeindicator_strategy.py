import backtrader as bt
from ..base_strategy import FlexibleStrategy

class DeltaProfile_TrueRangeIndicator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von DeltaProfile und TrueRangeIndicator
    """
    
    params = (
        ('indicators', {
            'DeltaProfile': {
                'class': DeltaProfile,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_DeltaProfile'>
            },
            'TrueRangeIndicator': {
                'class': TrueRangeIndicator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TrueRangeIndicator'>
            }
        }),
        ('weights', {
            'DeltaProfile': 1.0,
            'TrueRangeIndicator': 1.0
        })
    )
