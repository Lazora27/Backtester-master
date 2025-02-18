import backtrader as bt
from ..base_strategy import FlexibleStrategy

class ModifiedRSI_BradleySiderograph_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von ModifiedRSI und BradleySiderograph
    """
    
    params = (
        ('indicators', {
            'ModifiedRSI': {
                'class': ModifiedRSI,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ModifiedRSI'>
            },
            'BradleySiderograph': {
                'class': BradleySiderograph,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_BradleySiderograph'>
            }
        }),
        ('weights', {
            'ModifiedRSI': 1.0,
            'BradleySiderograph': 1.0
        })
    )
