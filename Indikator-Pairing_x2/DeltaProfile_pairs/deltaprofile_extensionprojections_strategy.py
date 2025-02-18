import backtrader as bt
from ..base_strategy import FlexibleStrategy

class DeltaProfile_ExtensionProjections_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von DeltaProfile und ExtensionProjections
    """
    
    params = (
        ('indicators', {
            'DeltaProfile': {
                'class': DeltaProfile,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_DeltaProfile'>
            },
            'ExtensionProjections': {
                'class': ExtensionProjections,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ExtensionProjections'>
            }
        }),
        ('weights', {
            'DeltaProfile': 1.0,
            'ExtensionProjections': 1.0
        })
    )
