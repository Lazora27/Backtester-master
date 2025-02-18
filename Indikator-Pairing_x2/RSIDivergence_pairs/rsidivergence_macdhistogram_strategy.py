import backtrader as bt
from ..base_strategy import FlexibleStrategy

class RSIDivergence_MACDHistogram_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von RSIDivergence und MACDHistogram
    """
    
    params = (
        ('indicators', {
            'RSIDivergence': {
                'class': RSIDivergence,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_RSIDivergence'>
            },
            'MACDHistogram': {
                'class': MACDHistogram,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MACDHistogram'>
            }
        }),
        ('weights', {
            'RSIDivergence': 1.0,
            'MACDHistogram': 1.0
        })
    )
