import backtrader as bt
from ..base_strategy import FlexibleStrategy

class DeltaProfile_TrueRange_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von DeltaProfile und TrueRange
    """
    
    params = (
        ('indicators', {
            'DeltaProfile': {
                'class': DeltaProfile,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_DeltaProfile'>
            },
            'TrueRange': {
                'class': TrueRange,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TrueRange1'>
            }
        }),
        ('weights', {
            'DeltaProfile': 1.0,
            'TrueRange': 1.0
        })
    )
