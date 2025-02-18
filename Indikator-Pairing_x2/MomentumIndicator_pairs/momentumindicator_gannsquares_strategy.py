import backtrader as bt
from ..base_strategy import FlexibleStrategy

class MomentumIndicator_GannSquares_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von MomentumIndicator und GannSquares
    """
    
    params = (
        ('indicators', {
            'MomentumIndicator': {
                'class': MomentumIndicator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MomentumIndicator'>
            },
            'GannSquares': {
                'class': GannSquares,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_GannSquares'>
            }
        }),
        ('weights', {
            'MomentumIndicator': 1.0,
            'GannSquares': 1.0
        })
    )
