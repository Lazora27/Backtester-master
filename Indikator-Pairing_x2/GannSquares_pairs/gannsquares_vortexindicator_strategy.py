import backtrader as bt
from ..base_strategy import FlexibleStrategy

class GannSquares_VortexIndicator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von GannSquares und VortexIndicator
    """
    
    params = (
        ('indicators', {
            'GannSquares': {
                'class': GannSquares,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_GannSquares'>
            },
            'VortexIndicator': {
                'class': VortexIndicator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_VortexIndicator'>
            }
        }),
        ('weights', {
            'GannSquares': 1.0,
            'VortexIndicator': 1.0
        })
    )
