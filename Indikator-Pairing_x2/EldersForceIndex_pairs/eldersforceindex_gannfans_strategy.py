import backtrader as bt
from ..base_strategy import FlexibleStrategy

class EldersForceIndex_GannFans_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von EldersForceIndex und GannFans
    """
    
    params = (
        ('indicators', {
            'EldersForceIndex': {
                'class': EldersForceIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_EldersForceIndex'>
            },
            'GannFans': {
                'class': GannFans,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_GannFans'>
            }
        }),
        ('weights', {
            'EldersForceIndex': 1.0,
            'GannFans': 1.0
        })
    )
