import backtrader as bt
from ..base_strategy import FlexibleStrategy

class AdaptiveATR_BradleySiderograph_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von AdaptiveATR und BradleySiderograph
    """
    
    params = (
        ('indicators', {
            'AdaptiveATR': {
                'class': AdaptiveATR,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AdaptiveATR'>
            },
            'BradleySiderograph': {
                'class': BradleySiderograph,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_BradleySiderograph'>
            }
        }),
        ('weights', {
            'AdaptiveATR': 1.0,
            'BradleySiderograph': 1.0
        })
    )
