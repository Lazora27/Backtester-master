import backtrader as bt
from ..base_strategy import FlexibleStrategy

class TickIndex_VWAPBands_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von TickIndex und VWAPBands
    """
    
    params = (
        ('indicators', {
            'TickIndex': {
                'class': TickIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TickIndex'>
            },
            'VWAPBands': {
                'class': VWAPBands,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_VWAPBands'>
            }
        }),
        ('weights', {
            'TickIndex': 1.0,
            'VWAPBands': 1.0
        })
    )
