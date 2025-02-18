import backtrader as bt
from ..base_strategy import FlexibleStrategy

class TrueStrengthIndex_HilbertTrendline_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von TrueStrengthIndex und HilbertTrendline
    """
    
    params = (
        ('indicators', {
            'TrueStrengthIndex': {
                'class': TrueStrengthIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TrueStrengthIndex'>
            },
            'HilbertTrendline': {
                'class': HilbertTrendline,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HilbertTrendline'>
            }
        }),
        ('weights', {
            'TrueStrengthIndex': 1.0,
            'HilbertTrendline': 1.0
        })
    )
