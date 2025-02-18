import backtrader as bt
from ..base_strategy import FlexibleStrategy

class ChandeKrollStop_BradleySiderograph_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von ChandeKrollStop und BradleySiderograph
    """
    
    params = (
        ('indicators', {
            'ChandeKrollStop': {
                'class': ChandeKrollStop,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ChandeKrollStop'>
            },
            'BradleySiderograph': {
                'class': BradleySiderograph,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_BradleySiderograph'>
            }
        }),
        ('weights', {
            'ChandeKrollStop': 1.0,
            'BradleySiderograph': 1.0
        })
    )
