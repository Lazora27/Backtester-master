import backtrader as bt
from ..base_strategy import FlexibleStrategy

class DeltaProfile_GannFans_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von DeltaProfile und GannFans
    """
    
    params = (
        ('indicators', {
            'DeltaProfile': {
                'class': DeltaProfile,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_DeltaProfile'>
            },
            'GannFans': {
                'class': GannFans,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_GannFans'>
            }
        }),
        ('weights', {
            'DeltaProfile': 1.0,
            'GannFans': 1.0
        })
    )
