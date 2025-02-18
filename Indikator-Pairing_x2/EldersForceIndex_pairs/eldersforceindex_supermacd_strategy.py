import backtrader as bt
from ..base_strategy import FlexibleStrategy

class EldersForceIndex_SuperMACD_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von EldersForceIndex und SuperMACD
    """
    
    params = (
        ('indicators', {
            'EldersForceIndex': {
                'class': EldersForceIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_EldersForceIndex'>
            },
            'SuperMACD': {
                'class': SuperMACD,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SuperMACD'>
            }
        }),
        ('weights', {
            'EldersForceIndex': 1.0,
            'SuperMACD': 1.0
        })
    )
