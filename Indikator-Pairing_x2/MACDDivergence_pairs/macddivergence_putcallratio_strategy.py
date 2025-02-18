import backtrader as bt
from ..base_strategy import FlexibleStrategy

class MACDDivergence_PutCallRatio_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von MACDDivergence und PutCallRatio
    """
    
    params = (
        ('indicators', {
            'MACDDivergence': {
                'class': MACDDivergence,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MACDDivergence'>
            },
            'PutCallRatio': {
                'class': PutCallRatio,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PutCallRatio1'>
            }
        }),
        ('weights', {
            'MACDDivergence': 1.0,
            'PutCallRatio': 1.0
        })
    )
