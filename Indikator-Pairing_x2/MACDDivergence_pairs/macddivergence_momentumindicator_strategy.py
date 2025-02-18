import backtrader as bt
from ..base_strategy import FlexibleStrategy

class MACDDivergence_MomentumIndicator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von MACDDivergence und MomentumIndicator
    """
    
    params = (
        ('indicators', {
            'MACDDivergence': {
                'class': MACDDivergence,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MACDDivergence'>
            },
            'MomentumIndicator': {
                'class': MomentumIndicator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MomentumIndicator'>
            }
        }),
        ('weights', {
            'MACDDivergence': 1.0,
            'MomentumIndicator': 1.0
        })
    )
