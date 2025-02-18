import backtrader as bt
from ..base_strategy import FlexibleStrategy

class VolatilityIndex_HilbertTrendline_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von VolatilityIndex und HilbertTrendline
    """
    
    params = (
        ('indicators', {
            'VolatilityIndex': {
                'class': VolatilityIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_VolatilityIndex'>
            },
            'HilbertTrendline': {
                'class': HilbertTrendline,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HilbertTrendline'>
            }
        }),
        ('weights', {
            'VolatilityIndex': 1.0,
            'HilbertTrendline': 1.0
        })
    )
