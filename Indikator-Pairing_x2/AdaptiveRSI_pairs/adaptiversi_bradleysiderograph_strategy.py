import backtrader as bt
from ..base_strategy import FlexibleStrategy

class AdaptiveRSI_BradleySiderograph_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von AdaptiveRSI und BradleySiderograph
    """
    
    params = (
        ('indicators', {
            'AdaptiveRSI': {
                'class': AdaptiveRSI,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AdaptiveRSI'>
            },
            'BradleySiderograph': {
                'class': BradleySiderograph,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_BradleySiderograph'>
            }
        }),
        ('weights', {
            'AdaptiveRSI': 1.0,
            'BradleySiderograph': 1.0
        })
    )
