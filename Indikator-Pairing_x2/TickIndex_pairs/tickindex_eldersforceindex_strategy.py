import backtrader as bt
from ..base_strategy import FlexibleStrategy

class TickIndex_EldersForceIndex_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von TickIndex und EldersForceIndex
    """
    
    params = (
        ('indicators', {
            'TickIndex': {
                'class': TickIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TickIndex'>
            },
            'EldersForceIndex': {
                'class': EldersForceIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_EldersForceIndex'>
            }
        }),
        ('weights', {
            'TickIndex': 1.0,
            'EldersForceIndex': 1.0
        })
    )
