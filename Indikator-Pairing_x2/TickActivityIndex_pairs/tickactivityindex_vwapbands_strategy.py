import backtrader as bt
from ..base_strategy import FlexibleStrategy

class TickActivityIndex_VWAPBands_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von TickActivityIndex und VWAPBands
    """
    
    params = (
        ('indicators', {
            'TickActivityIndex': {
                'class': TickActivityIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TickActivityIndex'>
            },
            'VWAPBands': {
                'class': VWAPBands,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_VWAPBands'>
            }
        }),
        ('weights', {
            'TickActivityIndex': 1.0,
            'VWAPBands': 1.0
        })
    )
