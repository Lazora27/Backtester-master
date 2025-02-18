import backtrader as bt
from ..base_strategy import FlexibleStrategy

class HilbertTrendline_TimeCycle_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von HilbertTrendline und TimeCycle
    """
    
    params = (
        ('indicators', {
            'HilbertTrendline': {
                'class': HilbertTrendline,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HilbertTrendline'>
            },
            'TimeCycle': {
                'class': TimeCycle,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TimeCycle'>
            }
        }),
        ('weights', {
            'HilbertTrendline': 1.0,
            'TimeCycle': 1.0
        })
    )
