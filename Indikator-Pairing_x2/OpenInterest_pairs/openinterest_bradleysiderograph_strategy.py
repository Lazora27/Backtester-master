import backtrader as bt
from ..base_strategy import FlexibleStrategy

class OpenInterest_BradleySiderograph_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von OpenInterest und BradleySiderograph
    """
    
    params = (
        ('indicators', {
            'OpenInterest': {
                'class': OpenInterest,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_OpenInterest'>
            },
            'BradleySiderograph': {
                'class': BradleySiderograph,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_BradleySiderograph'>
            }
        }),
        ('weights', {
            'OpenInterest': 1.0,
            'BradleySiderograph': 1.0
        })
    )
