import backtrader as bt
from ..base_strategy import FlexibleStrategy

class HistoricalATR_AccelerationBands_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von HistoricalATR und AccelerationBands
    """
    
    params = (
        ('indicators', {
            'HistoricalATR': {
                'class': HistoricalATR,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HistoricalATR'>
            },
            'AccelerationBands': {
                'class': AccelerationBands,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AccelerationBands'>
            }
        }),
        ('weights', {
            'HistoricalATR': 1.0,
            'AccelerationBands': 1.0
        })
    )
