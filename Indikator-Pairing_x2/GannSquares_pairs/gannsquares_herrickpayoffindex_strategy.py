import backtrader as bt
from ..base_strategy import FlexibleStrategy

class GannSquares_HerrickPayoffIndex_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von GannSquares und HerrickPayoffIndex
    """
    
    params = (
        ('indicators', {
            'GannSquares': {
                'class': GannSquares,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_GannSquares'>
            },
            'HerrickPayoffIndex': {
                'class': HerrickPayoffIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HerrickPayoffIndex'>
            }
        }),
        ('weights', {
            'GannSquares': 1.0,
            'HerrickPayoffIndex': 1.0
        })
    )
