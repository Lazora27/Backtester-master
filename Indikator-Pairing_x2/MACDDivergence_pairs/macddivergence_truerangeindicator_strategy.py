import backtrader as bt
from ..base_strategy import FlexibleStrategy

class MACDDivergence_TrueRangeIndicator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von MACDDivergence und TrueRangeIndicator
    """
    
    params = (
        ('indicators', {
            'MACDDivergence': {
                'class': MACDDivergence,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MACDDivergence'>
            },
            'TrueRangeIndicator': {
                'class': TrueRangeIndicator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TrueRangeIndicator'>
            }
        }),
        ('weights', {
            'MACDDivergence': 1.0,
            'TrueRangeIndicator': 1.0
        })
    )
