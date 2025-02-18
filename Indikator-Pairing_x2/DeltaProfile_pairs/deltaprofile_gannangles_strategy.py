import backtrader as bt
from ..base_strategy import FlexibleStrategy

class DeltaProfile_GannAngles_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von DeltaProfile und GannAngles
    """
    
    params = (
        ('indicators', {
            'DeltaProfile': {
                'class': DeltaProfile,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_DeltaProfile'>
            },
            'GannAngles': {
                'class': GannAngles,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_GannAngles1'>
            }
        }),
        ('weights', {
            'DeltaProfile': 1.0,
            'GannAngles': 1.0
        })
    )
