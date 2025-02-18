import backtrader as bt
from ..base_strategy import FlexibleStrategy

class TickVolume_DemandIndex_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von TickVolume und DemandIndex
    """
    
    params = (
        ('indicators', {
            'TickVolume': {
                'class': TickVolume,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TickVolume'>
            },
            'DemandIndex': {
                'class': DemandIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_DemandIndex'>
            }
        }),
        ('weights', {
            'TickVolume': 1.0,
            'DemandIndex': 1.0
        })
    )
