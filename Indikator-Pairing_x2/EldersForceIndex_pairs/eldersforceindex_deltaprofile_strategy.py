import backtrader as bt
from ..base_strategy import FlexibleStrategy

class EldersForceIndex_DeltaProfile_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von EldersForceIndex und DeltaProfile
    """
    
    params = (
        ('indicators', {
            'EldersForceIndex': {
                'class': EldersForceIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_EldersForceIndex'>
            },
            'DeltaProfile': {
                'class': DeltaProfile,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_DeltaProfile'>
            }
        }),
        ('weights', {
            'EldersForceIndex': 1.0,
            'DeltaProfile': 1.0
        })
    )
