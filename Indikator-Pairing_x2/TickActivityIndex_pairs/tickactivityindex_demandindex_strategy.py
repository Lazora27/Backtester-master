import backtrader as bt
from ..base_strategy import FlexibleStrategy

class TickActivityIndex_DemandIndex_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von TickActivityIndex und DemandIndex
    """
    
    params = (
        ('indicators', {
            'TickActivityIndex': {
                'class': TickActivityIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TickActivityIndex'>
            },
            'DemandIndex': {
                'class': DemandIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_DemandIndex'>
            }
        }),
        ('weights', {
            'TickActivityIndex': 1.0,
            'DemandIndex': 1.0
        })
    )
