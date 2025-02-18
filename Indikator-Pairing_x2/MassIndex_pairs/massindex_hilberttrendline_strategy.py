import backtrader as bt
from ..base_strategy import FlexibleStrategy

class MassIndex_HilbertTrendline_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von MassIndex und HilbertTrendline
    """
    
    params = (
        ('indicators', {
            'MassIndex': {
                'class': MassIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MassIndex'>
            },
            'HilbertTrendline': {
                'class': HilbertTrendline,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HilbertTrendline'>
            }
        }),
        ('weights', {
            'MassIndex': 1.0,
            'HilbertTrendline': 1.0
        })
    )
