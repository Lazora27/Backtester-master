import backtrader as bt
from ..base_strategy import FlexibleStrategy

class EldersForceIndex_Fisher_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von EldersForceIndex und Fisher
    """
    
    params = (
        ('indicators', {
            'EldersForceIndex': {
                'class': EldersForceIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_EldersForceIndex'>
            },
            'Fisher': {
                'class': Fisher,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_Fisher'>
            }
        }),
        ('weights', {
            'EldersForceIndex': 1.0,
            'Fisher': 1.0
        })
    )
