import backtrader as bt
from ..base_strategy import FlexibleStrategy

class VWAPDeviationBands_HilbertTrendline_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von VWAPDeviationBands und HilbertTrendline
    """
    
    params = (
        ('indicators', {
            'VWAPDeviationBands': {
                'class': VWAPDeviationBands,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_VWAPDeviationBands'>
            },
            'HilbertTrendline': {
                'class': HilbertTrendline,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HilbertTrendline'>
            }
        }),
        ('weights', {
            'VWAPDeviationBands': 1.0,
            'HilbertTrendline': 1.0
        })
    )
