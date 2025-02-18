import backtrader as bt
from ..base_strategy import FlexibleStrategy

class MACDDivergence_HilbertTrendline_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von MACDDivergence und HilbertTrendline
    """
    
    params = (
        ('indicators', {
            'MACDDivergence': {
                'class': MACDDivergence,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MACDDivergence'>
            },
            'HilbertTrendline': {
                'class': HilbertTrendline,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HilbertTrendline'>
            }
        }),
        ('weights', {
            'MACDDivergence': 1.0,
            'HilbertTrendline': 1.0
        })
    )
