import backtrader as bt
from ..base_strategy import FlexibleStrategy

class EldersForceIndex_GannAngles_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von EldersForceIndex und GannAngles
    """
    
    params = (
        ('indicators', {
            'EldersForceIndex': {
                'class': EldersForceIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_EldersForceIndex'>
            },
            'GannAngles': {
                'class': GannAngles,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_GannAngles1'>
            }
        }),
        ('weights', {
            'EldersForceIndex': 1.0,
            'GannAngles': 1.0
        })
    )
