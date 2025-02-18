import backtrader as bt
from ..base_strategy import FlexibleStrategy

class SmoothedRSI_DeltaProfile_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von SmoothedRSI und DeltaProfile
    """
    
    params = (
        ('indicators', {
            'SmoothedRSI': {
                'class': SmoothedRSI,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SmoothedRSI'>
            },
            'DeltaProfile': {
                'class': DeltaProfile,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_DeltaProfile'>
            }
        }),
        ('weights', {
            'SmoothedRSI': 1.0,
            'DeltaProfile': 1.0
        })
    )
