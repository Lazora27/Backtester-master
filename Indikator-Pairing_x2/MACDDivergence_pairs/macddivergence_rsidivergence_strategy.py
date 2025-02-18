import backtrader as bt
from ..base_strategy import FlexibleStrategy

class MACDDivergence_RSIDivergence_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von MACDDivergence und RSIDivergence
    """
    
    params = (
        ('indicators', {
            'MACDDivergence': {
                'class': MACDDivergence,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MACDDivergence'>
            },
            'RSIDivergence': {
                'class': RSIDivergence,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_RSIDivergence'>
            }
        }),
        ('weights', {
            'MACDDivergence': 1.0,
            'RSIDivergence': 1.0
        })
    )
