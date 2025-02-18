import backtrader as bt
from ..base_strategy import FlexibleStrategy

class RelativeVigorIndex_HilbertTrendline_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von RelativeVigorIndex und HilbertTrendline
    """
    
    params = (
        ('indicators', {
            'RelativeVigorIndex': {
                'class': RelativeVigorIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_RelativeVigorIndex'>
            },
            'HilbertTrendline': {
                'class': HilbertTrendline,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HilbertTrendline'>
            }
        }),
        ('weights', {
            'RelativeVigorIndex': 1.0,
            'HilbertTrendline': 1.0
        })
    )
