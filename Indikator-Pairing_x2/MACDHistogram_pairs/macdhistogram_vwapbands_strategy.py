import backtrader as bt
from ..base_strategy import FlexibleStrategy

class MACDHistogram_VWAPBands_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von MACDHistogram und VWAPBands
    """
    
    params = (
        ('indicators', {
            'MACDHistogram': {
                'class': MACDHistogram,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MACDHistogram'>
            },
            'VWAPBands': {
                'class': VWAPBands,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_VWAPBands'>
            }
        }),
        ('weights', {
            'MACDHistogram': 1.0,
            'VWAPBands': 1.0
        })
    )
