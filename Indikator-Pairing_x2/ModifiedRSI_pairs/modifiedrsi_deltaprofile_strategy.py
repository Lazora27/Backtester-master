import backtrader as bt
from ..base_strategy import FlexibleStrategy

class ModifiedRSI_DeltaProfile_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von ModifiedRSI und DeltaProfile
    """
    
    params = (
        ('indicators', {
            'ModifiedRSI': {
                'class': ModifiedRSI,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ModifiedRSI'>
            },
            'DeltaProfile': {
                'class': DeltaProfile,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_DeltaProfile'>
            }
        }),
        ('weights', {
            'ModifiedRSI': 1.0,
            'DeltaProfile': 1.0
        })
    )
