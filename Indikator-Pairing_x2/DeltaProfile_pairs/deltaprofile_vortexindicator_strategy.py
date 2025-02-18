import backtrader as bt
from ..base_strategy import FlexibleStrategy

class DeltaProfile_VortexIndicator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von DeltaProfile und VortexIndicator
    """
    
    params = (
        ('indicators', {
            'DeltaProfile': {
                'class': DeltaProfile,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_DeltaProfile'>
            },
            'VortexIndicator': {
                'class': VortexIndicator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_VortexIndicator'>
            }
        }),
        ('weights', {
            'DeltaProfile': 1.0,
            'VortexIndicator': 1.0
        })
    )
