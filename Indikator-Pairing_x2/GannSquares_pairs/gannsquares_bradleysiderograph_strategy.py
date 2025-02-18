import backtrader as bt
from ..base_strategy import FlexibleStrategy

class GannSquares_BradleySiderograph_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von GannSquares und BradleySiderograph
    """
    
    params = (
        ('indicators', {
            'GannSquares': {
                'class': GannSquares,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_GannSquares'>
            },
            'BradleySiderograph': {
                'class': BradleySiderograph,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_BradleySiderograph'>
            }
        }),
        ('weights', {
            'GannSquares': 1.0,
            'BradleySiderograph': 1.0
        })
    )
