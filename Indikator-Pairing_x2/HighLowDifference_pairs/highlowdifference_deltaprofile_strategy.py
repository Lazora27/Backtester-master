import backtrader as bt
from ..base_strategy import FlexibleStrategy

class HighLowDifference_DeltaProfile_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von HighLowDifference und DeltaProfile
    """
    
    params = (
        ('indicators', {
            'HighLowDifference': {
                'class': HighLowDifference,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HighLowDifference'>
            },
            'DeltaProfile': {
                'class': DeltaProfile,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_DeltaProfile'>
            }
        }),
        ('weights', {
            'HighLowDifference': 1.0,
            'DeltaProfile': 1.0
        })
    )
