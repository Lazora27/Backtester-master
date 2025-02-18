import backtrader as bt
from ..base_strategy import FlexibleStrategy

class RelativeStrengthIndex_HilbertTrendline_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von RelativeStrengthIndex und HilbertTrendline
    """
    
    params = (
        ('indicators', {
            'RelativeStrengthIndex': {
                'class': RelativeStrengthIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_RelativeStrengthIndex1'>
            },
            'HilbertTrendline': {
                'class': HilbertTrendline,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HilbertTrendline'>
            }
        }),
        ('weights', {
            'RelativeStrengthIndex': 1.0,
            'HilbertTrendline': 1.0
        })
    )
