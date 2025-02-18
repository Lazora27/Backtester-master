import backtrader as bt
from ..base_strategy import FlexibleStrategy

class DeltaProfile_NormalizedAverageTrueRange_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von DeltaProfile und NormalizedAverageTrueRange
    """
    
    params = (
        ('indicators', {
            'DeltaProfile': {
                'class': DeltaProfile,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_DeltaProfile'>
            },
            'NormalizedAverageTrueRange': {
                'class': NormalizedAverageTrueRange,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_NormalizedAverageTrueRange'>
            }
        }),
        ('weights', {
            'DeltaProfile': 1.0,
            'NormalizedAverageTrueRange': 1.0
        })
    )
