import backtrader as bt
from ..base_strategy import FlexibleStrategy

class MomentumIndicator_GannSquareReversal_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von MomentumIndicator und GannSquareReversal
    """
    
    params = (
        ('indicators', {
            'MomentumIndicator': {
                'class': MomentumIndicator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MomentumIndicator'>
            },
            'GannSquareReversal': {
                'class': GannSquareReversal,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_GannSquareReversal'>
            }
        }),
        ('weights', {
            'MomentumIndicator': 1.0,
            'GannSquareReversal': 1.0
        })
    )
