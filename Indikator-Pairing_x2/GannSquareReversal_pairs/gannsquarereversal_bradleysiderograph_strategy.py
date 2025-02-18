import backtrader as bt
from ..base_strategy import FlexibleStrategy

class GannSquareReversal_BradleySiderograph_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von GannSquareReversal und BradleySiderograph
    """
    
    params = (
        ('indicators', {
            'GannSquareReversal': {
                'class': GannSquareReversal,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_GannSquareReversal'>
            },
            'BradleySiderograph': {
                'class': BradleySiderograph,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_BradleySiderograph'>
            }
        }),
        ('weights', {
            'GannSquareReversal': 1.0,
            'BradleySiderograph': 1.0
        })
    )
