import backtrader as bt
from ..base_strategy import FlexibleStrategy

class MomentumIndicator_TickActivityIndex_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von MomentumIndicator und TickActivityIndex
    """
    
    params = (
        ('indicators', {
            'MomentumIndicator': {
                'class': MomentumIndicator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MomentumIndicator'>
            },
            'TickActivityIndex': {
                'class': TickActivityIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TickActivityIndex'>
            }
        }),
        ('weights', {
            'MomentumIndicator': 1.0,
            'TickActivityIndex': 1.0
        })
    )
