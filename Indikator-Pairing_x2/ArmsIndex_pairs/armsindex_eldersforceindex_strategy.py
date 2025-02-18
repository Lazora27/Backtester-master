import backtrader as bt
from ..base_strategy import FlexibleStrategy

class ArmsIndex_EldersForceIndex_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von ArmsIndex und EldersForceIndex
    """
    
    params = (
        ('indicators', {
            'ArmsIndex': {
                'class': ArmsIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ArmsIndex'>
            },
            'EldersForceIndex': {
                'class': EldersForceIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_EldersForceIndex'>
            }
        }),
        ('weights', {
            'ArmsIndex': 1.0,
            'EldersForceIndex': 1.0
        })
    )
