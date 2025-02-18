import backtrader as bt
from ..base_strategy import FlexibleStrategy

class HighLowIndex_AccelerationBands_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von HighLowIndex und AccelerationBands
    """
    
    params = (
        ('indicators', {
            'HighLowIndex': {
                'class': HighLowIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HighLowIndex'>
            },
            'AccelerationBands': {
                'class': AccelerationBands,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AccelerationBands'>
            }
        }),
        ('weights', {
            'HighLowIndex': 1.0,
            'AccelerationBands': 1.0
        })
    )
