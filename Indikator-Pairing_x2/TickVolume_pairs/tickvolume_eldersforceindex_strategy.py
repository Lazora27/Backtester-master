import backtrader as bt
from ..base_strategy import FlexibleStrategy

class TickVolume_EldersForceIndex_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von TickVolume und EldersForceIndex
    """
    
    params = (
        ('indicators', {
            'TickVolume': {
                'class': TickVolume,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TickVolume'>
            },
            'EldersForceIndex': {
                'class': EldersForceIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_EldersForceIndex'>
            }
        }),
        ('weights', {
            'TickVolume': 1.0,
            'EldersForceIndex': 1.0
        })
    )
