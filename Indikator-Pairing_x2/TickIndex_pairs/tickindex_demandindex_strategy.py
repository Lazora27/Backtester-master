import backtrader as bt
from ..base_strategy import FlexibleStrategy

class TickIndex_DemandIndex_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von TickIndex und DemandIndex
    """
    
    params = (
        ('indicators', {
            'TickIndex': {
                'class': TickIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TickIndex'>
            },
            'DemandIndex': {
                'class': DemandIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_DemandIndex'>
            }
        }),
        ('weights', {
            'TickIndex': 1.0,
            'DemandIndex': 1.0
        })
    )
