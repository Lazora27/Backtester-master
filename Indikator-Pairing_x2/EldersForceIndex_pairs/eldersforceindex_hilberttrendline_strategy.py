import backtrader as bt
from ..base_strategy import FlexibleStrategy

class EldersForceIndex_HilbertTrendline_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von EldersForceIndex und HilbertTrendline
    """
    
    params = (
        ('indicators', {
            'EldersForceIndex': {
                'class': EldersForceIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_EldersForceIndex'>
            },
            'HilbertTrendline': {
                'class': HilbertTrendline,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HilbertTrendline'>
            }
        }),
        ('weights', {
            'EldersForceIndex': 1.0,
            'HilbertTrendline': 1.0
        })
    )
