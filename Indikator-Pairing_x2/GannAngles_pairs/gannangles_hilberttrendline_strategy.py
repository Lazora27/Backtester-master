import backtrader as bt
from ..base_strategy import FlexibleStrategy

class GannAngles_HilbertTrendline_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von GannAngles und HilbertTrendline
    """
    
    params = (
        ('indicators', {
            'GannAngles': {
                'class': GannAngles,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_GannAngles1'>
            },
            'HilbertTrendline': {
                'class': HilbertTrendline,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HilbertTrendline'>
            }
        }),
        ('weights', {
            'GannAngles': 1.0,
            'HilbertTrendline': 1.0
        })
    )
