import backtrader as bt
from ..base_strategy import FlexibleStrategy

class MACDDivergence_SmoothedCycle_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von MACDDivergence und SmoothedCycle
    """
    
    params = (
        ('indicators', {
            'MACDDivergence': {
                'class': MACDDivergence,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MACDDivergence'>
            },
            'SmoothedCycle': {
                'class': SmoothedCycle,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SmoothedCycle'>
            }
        }),
        ('weights', {
            'MACDDivergence': 1.0,
            'SmoothedCycle': 1.0
        })
    )
