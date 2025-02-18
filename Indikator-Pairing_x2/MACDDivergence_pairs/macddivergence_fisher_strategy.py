import backtrader as bt
from ..base_strategy import FlexibleStrategy

class MACDDivergence_Fisher_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von MACDDivergence und Fisher
    """
    
    params = (
        ('indicators', {
            'MACDDivergence': {
                'class': MACDDivergence,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MACDDivergence'>
            },
            'Fisher': {
                'class': Fisher,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_Fisher'>
            }
        }),
        ('weights', {
            'MACDDivergence': 1.0,
            'Fisher': 1.0
        })
    )
