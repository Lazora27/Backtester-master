import backtrader as bt
from ..base_strategy import FlexibleStrategy

class MACDDivergence_TickActivityIndex_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von MACDDivergence und TickActivityIndex
    """
    
    params = (
        ('indicators', {
            'MACDDivergence': {
                'class': MACDDivergence,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MACDDivergence'>
            },
            'TickActivityIndex': {
                'class': TickActivityIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TickActivityIndex'>
            }
        }),
        ('weights', {
            'MACDDivergence': 1.0,
            'TickActivityIndex': 1.0
        })
    )
