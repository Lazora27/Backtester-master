import backtrader as bt
from ..base_strategy import FlexibleStrategy

class MACDDivergence_TrueRange_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von MACDDivergence und TrueRange
    """
    
    params = (
        ('indicators', {
            'MACDDivergence': {
                'class': MACDDivergence,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MACDDivergence'>
            },
            'TrueRange': {
                'class': TrueRange,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TrueRange1'>
            }
        }),
        ('weights', {
            'MACDDivergence': 1.0,
            'TrueRange': 1.0
        })
    )
