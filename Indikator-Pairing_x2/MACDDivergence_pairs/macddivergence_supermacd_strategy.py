import backtrader as bt
from ..base_strategy import FlexibleStrategy

class MACDDivergence_SuperMACD_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von MACDDivergence und SuperMACD
    """
    
    params = (
        ('indicators', {
            'MACDDivergence': {
                'class': MACDDivergence,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MACDDivergence'>
            },
            'SuperMACD': {
                'class': SuperMACD,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SuperMACD'>
            }
        }),
        ('weights', {
            'MACDDivergence': 1.0,
            'SuperMACD': 1.0
        })
    )
