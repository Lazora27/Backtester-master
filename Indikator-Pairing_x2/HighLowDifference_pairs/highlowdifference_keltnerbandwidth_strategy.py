import backtrader as bt
from ..base_strategy import FlexibleStrategy

class HighLowDifference_KeltnerBandWidth_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von HighLowDifference und KeltnerBandWidth
    """
    
    params = (
        ('indicators', {
            'HighLowDifference': {
                'class': HighLowDifference,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HighLowDifference'>
            },
            'KeltnerBandWidth': {
                'class': KeltnerBandWidth,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_KeltnerBandWidth'>
            }
        }),
        ('weights', {
            'HighLowDifference': 1.0,
            'KeltnerBandWidth': 1.0
        })
    )
