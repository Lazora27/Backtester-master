import backtrader as bt
from ..base_strategy import FlexibleStrategy

class MACDDivergence_AroonIndicator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von MACDDivergence und AroonIndicator
    """
    
    params = (
        ('indicators', {
            'MACDDivergence': {
                'class': MACDDivergence,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MACDDivergence'>
            },
            'AroonIndicator': {
                'class': AroonIndicator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AroonIndicator'>
            }
        }),
        ('weights', {
            'MACDDivergence': 1.0,
            'AroonIndicator': 1.0
        })
    )
