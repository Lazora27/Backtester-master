import backtrader as bt
from ..base_strategy import FlexibleStrategy

class EldersForceIndex_TickActivityIndex_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von EldersForceIndex und TickActivityIndex
    """
    
    params = (
        ('indicators', {
            'EldersForceIndex': {
                'class': EldersForceIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_EldersForceIndex'>
            },
            'TickActivityIndex': {
                'class': TickActivityIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TickActivityIndex'>
            }
        }),
        ('weights', {
            'EldersForceIndex': 1.0,
            'TickActivityIndex': 1.0
        })
    )
