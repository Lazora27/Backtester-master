import backtrader as bt
from ..base_strategy import FlexibleStrategy

class MACDDivergence_HighLowDifference_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von MACDDivergence und HighLowDifference
    """
    
    params = (
        ('indicators', {
            'MACDDivergence': {
                'class': MACDDivergence,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MACDDivergence'>
            },
            'HighLowDifference': {
                'class': HighLowDifference,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HighLowDifference'>
            }
        }),
        ('weights', {
            'MACDDivergence': 1.0,
            'HighLowDifference': 1.0
        })
    )
