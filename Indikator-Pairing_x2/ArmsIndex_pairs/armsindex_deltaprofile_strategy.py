import backtrader as bt
from ..base_strategy import FlexibleStrategy

class ArmsIndex_DeltaProfile_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von ArmsIndex und DeltaProfile
    """
    
    params = (
        ('indicators', {
            'ArmsIndex': {
                'class': ArmsIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ArmsIndex'>
            },
            'DeltaProfile': {
                'class': DeltaProfile,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_DeltaProfile'>
            }
        }),
        ('weights', {
            'ArmsIndex': 1.0,
            'DeltaProfile': 1.0
        })
    )
