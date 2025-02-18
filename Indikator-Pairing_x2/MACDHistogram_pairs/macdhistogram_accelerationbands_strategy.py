import backtrader as bt
from ..base_strategy import FlexibleStrategy

class MACDHistogram_AccelerationBands_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von MACDHistogram und AccelerationBands
    """
    
    params = (
        ('indicators', {
            'MACDHistogram': {
                'class': MACDHistogram,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MACDHistogram'>
            },
            'AccelerationBands': {
                'class': AccelerationBands,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AccelerationBands'>
            }
        }),
        ('weights', {
            'MACDHistogram': 1.0,
            'AccelerationBands': 1.0
        })
    )
