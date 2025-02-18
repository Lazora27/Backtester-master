import backtrader as bt
from ..base_strategy import FlexibleStrategy

class EldersForceIndex_CenterOfGravity_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von EldersForceIndex und CenterOfGravity
    """
    
    params = (
        ('indicators', {
            'EldersForceIndex': {
                'class': EldersForceIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_EldersForceIndex'>
            },
            'CenterOfGravity': {
                'class': CenterOfGravity,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CenterOfGravity'>
            }
        }),
        ('weights', {
            'EldersForceIndex': 1.0,
            'CenterOfGravity': 1.0
        })
    )
