import backtrader as bt
from ..base_strategy import FlexibleStrategy

class MACDDivergence_TickIndex_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von MACDDivergence und TickIndex
    """
    
    params = (
        ('indicators', {
            'MACDDivergence': {
                'class': MACDDivergence,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MACDDivergence'>
            },
            'TickIndex': {
                'class': TickIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TickIndex'>
            }
        }),
        ('weights', {
            'MACDDivergence': 1.0,
            'TickIndex': 1.0
        })
    )
