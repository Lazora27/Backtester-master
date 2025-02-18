import backtrader as bt
from ..base_strategy import FlexibleStrategy

class TickIndex_MomentumIndicator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von TickIndex und MomentumIndicator
    """
    
    params = (
        ('indicators', {
            'TickIndex': {
                'class': TickIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TickIndex'>
            },
            'MomentumIndicator': {
                'class': MomentumIndicator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MomentumIndicator'>
            }
        }),
        ('weights', {
            'TickIndex': 1.0,
            'MomentumIndicator': 1.0
        })
    )
