import backtrader as bt
from ..base_strategy import FlexibleStrategy

class DemandIndex_HilbertTrendline_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von DemandIndex und HilbertTrendline
    """
    
    params = (
        ('indicators', {
            'DemandIndex': {
                'class': DemandIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_DemandIndex'>
            },
            'HilbertTrendline': {
                'class': HilbertTrendline,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HilbertTrendline'>
            }
        }),
        ('weights', {
            'DemandIndex': 1.0,
            'HilbertTrendline': 1.0
        })
    )
