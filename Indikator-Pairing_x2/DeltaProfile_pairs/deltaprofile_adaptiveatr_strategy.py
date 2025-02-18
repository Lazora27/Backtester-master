import backtrader as bt
from ..base_strategy import FlexibleStrategy

class DeltaProfile_AdaptiveATR_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von DeltaProfile und AdaptiveATR
    """
    
    params = (
        ('indicators', {
            'DeltaProfile': {
                'class': DeltaProfile,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_DeltaProfile'>
            },
            'AdaptiveATR': {
                'class': AdaptiveATR,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AdaptiveATR'>
            }
        }),
        ('weights', {
            'DeltaProfile': 1.0,
            'AdaptiveATR': 1.0
        })
    )
