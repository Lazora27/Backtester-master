import backtrader as bt
from ..base_strategy import FlexibleStrategy

class TickIndex_AccelerationBands_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von TickIndex und AccelerationBands
    """
    
    params = (
        ('indicators', {
            'TickIndex': {
                'class': TickIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TickIndex'>
            },
            'AccelerationBands': {
                'class': AccelerationBands,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AccelerationBands'>
            }
        }),
        ('weights', {
            'TickIndex': 1.0,
            'AccelerationBands': 1.0
        })
    )
