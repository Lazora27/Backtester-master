import backtrader as bt
from ..base_strategy import FlexibleStrategy

class VWAPBands_HilbertTrendline_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von VWAPBands und HilbertTrendline
    """
    
    params = (
        ('indicators', {
            'VWAPBands': {
                'class': VWAPBands,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_VWAPBands'>
            },
            'HilbertTrendline': {
                'class': HilbertTrendline,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HilbertTrendline'>
            }
        }),
        ('weights', {
            'VWAPBands': 1.0,
            'HilbertTrendline': 1.0
        })
    )
