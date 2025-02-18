import backtrader as bt
from ..base_strategy import FlexibleStrategy

class MACDDivergence_AdvanceDeclineLine_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von MACDDivergence und AdvanceDeclineLine
    """
    
    params = (
        ('indicators', {
            'MACDDivergence': {
                'class': MACDDivergence,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MACDDivergence'>
            },
            'AdvanceDeclineLine': {
                'class': AdvanceDeclineLine,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AdvanceDeclineLine'>
            }
        }),
        ('weights', {
            'MACDDivergence': 1.0,
            'AdvanceDeclineLine': 1.0
        })
    )
