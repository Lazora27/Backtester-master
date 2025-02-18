import backtrader as bt
from ..base_strategy import FlexibleStrategy

class MACDDivergence_KDJIndicator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von MACDDivergence und KDJIndicator
    """
    
    params = (
        ('indicators', {
            'MACDDivergence': {
                'class': MACDDivergence,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MACDDivergence'>
            },
            'KDJIndicator': {
                'class': KDJIndicator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_KDJIndicator'>
            }
        }),
        ('weights', {
            'MACDDivergence': 1.0,
            'KDJIndicator': 1.0
        })
    )
