import backtrader as bt
from ..base_strategy import FlexibleStrategy

class MACDDivergence_HighLowIndex_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von MACDDivergence und HighLowIndex
    """
    
    params = (
        ('indicators', {
            'MACDDivergence': {
                'class': MACDDivergence,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MACDDivergence'>
            },
            'HighLowIndex': {
                'class': HighLowIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HighLowIndex'>
            }
        }),
        ('weights', {
            'MACDDivergence': 1.0,
            'HighLowIndex': 1.0
        })
    )
