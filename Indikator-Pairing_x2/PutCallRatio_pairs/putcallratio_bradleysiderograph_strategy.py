import backtrader as bt
from ..base_strategy import FlexibleStrategy

class PutCallRatio_BradleySiderograph_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von PutCallRatio und BradleySiderograph
    """
    
    params = (
        ('indicators', {
            'PutCallRatio': {
                'class': PutCallRatio,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PutCallRatio1'>
            },
            'BradleySiderograph': {
                'class': BradleySiderograph,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_BradleySiderograph'>
            }
        }),
        ('weights', {
            'PutCallRatio': 1.0,
            'BradleySiderograph': 1.0
        })
    )
