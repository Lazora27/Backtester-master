import backtrader as bt
from ..base_strategy import FlexibleStrategy

class DeltaProfile_AdaptiveTrendLine_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von DeltaProfile und AdaptiveTrendLine
    """
    
    params = (
        ('indicators', {
            'DeltaProfile': {
                'class': DeltaProfile,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_DeltaProfile'>
            },
            'AdaptiveTrendLine': {
                'class': AdaptiveTrendLine,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AdaptiveTrendLine'>
            }
        }),
        ('weights', {
            'DeltaProfile': 1.0,
            'AdaptiveTrendLine': 1.0
        })
    )
