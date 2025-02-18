import backtrader as bt
from ..base_strategy import FlexibleStrategy

class GannSquareReversal_HerrickPayoffIndex_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von GannSquareReversal und HerrickPayoffIndex
    """
    
    params = (
        ('indicators', {
            'GannSquareReversal': {
                'class': GannSquareReversal,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_GannSquareReversal'>
            },
            'HerrickPayoffIndex': {
                'class': HerrickPayoffIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HerrickPayoffIndex'>
            }
        }),
        ('weights', {
            'GannSquareReversal': 1.0,
            'HerrickPayoffIndex': 1.0
        })
    )
