import backtrader as bt
from ..base_strategy import FlexibleStrategy

class DeltaProfile_SuperTrend_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von DeltaProfile und SuperTrend
    """
    
    params = (
        ('indicators', {
            'DeltaProfile': {
                'class': DeltaProfile,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_DeltaProfile'>
            },
            'SuperTrend': {
                'class': SuperTrend,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SuperTrend'>
            }
        }),
        ('weights', {
            'DeltaProfile': 1.0,
            'SuperTrend': 1.0
        })
    )
