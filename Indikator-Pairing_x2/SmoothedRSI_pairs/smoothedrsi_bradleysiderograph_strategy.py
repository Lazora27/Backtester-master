import backtrader as bt
from ..base_strategy import FlexibleStrategy

class SmoothedRSI_BradleySiderograph_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von SmoothedRSI und BradleySiderograph
    """
    
    params = (
        ('indicators', {
            'SmoothedRSI': {
                'class': SmoothedRSI,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SmoothedRSI'>
            },
            'BradleySiderograph': {
                'class': BradleySiderograph,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_BradleySiderograph'>
            }
        }),
        ('weights', {
            'SmoothedRSI': 1.0,
            'BradleySiderograph': 1.0
        })
    )
