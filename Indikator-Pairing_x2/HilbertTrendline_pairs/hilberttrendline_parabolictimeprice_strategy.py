import backtrader as bt
from ..base_strategy import FlexibleStrategy

class HilbertTrendline_ParabolicTimePrice_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von HilbertTrendline und ParabolicTimePrice
    """
    
    params = (
        ('indicators', {
            'HilbertTrendline': {
                'class': HilbertTrendline,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HilbertTrendline'>
            },
            'ParabolicTimePrice': {
                'class': ParabolicTimePrice,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ParabolicTimePrice'>
            }
        }),
        ('weights', {
            'HilbertTrendline': 1.0,
            'ParabolicTimePrice': 1.0
        })
    )
